"""Single-owner Linux executor. No model/API calls."""
import asyncio
import hashlib
import json
import os
import signal
import sqlite3
import time
from pathlib import Path

class Jobs:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.root.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(self.root / "jobs.sqlite")
        self.db.execute("CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, digest TEXT, state TEXT, code INTEGER, output TEXT, updated REAL)")
        self.db.execute("UPDATE jobs SET state='interrupted' WHERE state='running'")
        self.db.commit()
        self.active = {}
        self.tasks = set()

    def get(self, request_id, offset=0):
        row = self.db.execute("SELECT state,code,output,updated FROM jobs WHERE id=?", (request_id,)).fetchone()
        if row is None:
            raise ValueError("Unknown request_id")
        if offset < 0:
            raise ValueError("offset must be nonnegative")
        state, code, output, updated = row
        chunk = output[offset:offset + 16000]
        return dict(request_id=request_id, state=state, exit_code=code,
                    output=chunk, next_offset=offset + len(chunk),
                    updated=updated, untrusted_output=True)

    async def execute(self, request_id, argv, cwd=".", timeout=120):
        if not request_id or len(request_id) > 128:
            raise ValueError("request_id must contain 1..128 characters")
        if not argv or len(argv) > 100 or any(not isinstance(x, str) or "\0" in x for x in argv):
            raise ValueError("argv must be a nonempty string array")
        if not 1 <= timeout <= 900:
            raise ValueError("timeout must be 1..900 seconds")
        work = (self.root / cwd).resolve()
        if not work.is_relative_to(self.root) or not work.is_dir():
            raise ValueError("cwd must be a directory inside the work root")
        spec = json.dumps([argv, str(work), timeout], ensure_ascii=False)
        digest = hashlib.sha256(spec.encode()).hexdigest()
        old = self.db.execute("SELECT digest FROM jobs WHERE id=?", (request_id,)).fetchone()
        if old:
            if old[0] != digest:
                raise ValueError("request_id conflict: different command")
            return self.get(request_id)
        if self.active:
            raise ValueError("Executor busy; poll the existing job")
        self.db.execute("INSERT INTO jobs VALUES (?,?,?,NULL,?,?)",
                        (request_id, digest, "running", "", time.time()))
        self.db.commit()
        self.active[request_id] = None
        task = asyncio.create_task(self._run(request_id, argv, work, timeout))
        self.tasks.add(task)
        task.add_done_callback(self.tasks.discard)
        return self.get(request_id)

    def _save(self, request_id, state, code, output):
        self.db.execute("UPDATE jobs SET state=?,code=?,output=?,updated=? WHERE id=?",
                        (state, code, output, time.time(), request_id))
        self.db.commit()

    @staticmethod
    def _kill(proc):
        if proc is not None:
            try:
                os.killpg(proc.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass

    async def _run(self, request_id, argv, cwd, timeout):
        proc = None
        output = bytearray()
        state = "failed"
        code = None
        # Credentials for the gateway are deliberately not inherited.
        env = {k: os.environ[k] for k in ("PATH", "LANG", "HOME", "TMPDIR") if k in os.environ}
        env["PYTHONUNBUFFERED"] = "1"
        try:
            proc = await asyncio.create_subprocess_exec(*argv, cwd=cwd, env=env,
                stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.STDOUT,
                start_new_session=True)
            self.active[request_id] = proc
            async with asyncio.timeout(timeout):
                while True:
                    chunk = await proc.stdout.read(4096)
                    if not chunk:
                        break
                    output.extend(chunk)
                    if len(output) > 131072:
                        del output[131072:]
                        state = "output_limit"
                        self._kill(proc)
                        break
                    self._save(request_id, "running", None, output.decode("utf-8", "replace"))
                code = await proc.wait()
                if state != "output_limit":
                    state = "succeeded" if code == 0 else "failed"
        except TimeoutError:
            state = "timed_out"
        except asyncio.CancelledError:
            state = "cancelled"
        except (OSError, ValueError) as exc:
            output.extend(type(exc).__name__.encode())
        finally:
            self._kill(proc)  # Kill descendants even if the group leader exited.
            if proc:
                code = await proc.wait()
            self._save(request_id, state, code, output.decode("utf-8", "replace"))
            self.active.pop(request_id, None)

    async def cancel(self, request_id):
        if request_id in self.active:
            proc = self.active[request_id]
            self._kill(proc)
            # Cancel the worker too, including the pre-spawn window.
            for task in tuple(self.tasks):
                task.cancel()
            await asyncio.gather(*tuple(self.tasks), return_exceptions=True)
        return self.get(request_id)
