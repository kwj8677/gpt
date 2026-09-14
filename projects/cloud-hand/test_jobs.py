import asyncio
import sys
import tempfile
import unittest
from jobs import Jobs

class JobTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.jobs = Jobs(self.tmp.name)

    async def asyncTearDown(self):
        for key in tuple(self.jobs.active):
            await self.jobs.cancel(key)
        self.jobs.db.close()
        self.tmp.cleanup()

    async def finished(self, key):
        for _ in range(300):
            result = self.jobs.get(key)
            if result["state"] != "running":
                return result
            await asyncio.sleep(.01)
        self.fail("worker did not finish")

    async def test_retry_does_not_execute_twice(self):
        argv = [sys.executable, "-c", "from pathlib import Path; p=Path('count'); p.write_text(p.read_text()+'x' if p.exists() else 'x')"]
        await self.jobs.execute("one", argv)
        await self.finished("one")
        await self.jobs.execute("one", argv)
        self.assertEqual((self.jobs.root / "count").read_text(), "x")
        with self.assertRaises(ValueError):
            await self.jobs.execute("one", ["echo", "different"])

    async def test_failure_and_timeout(self):
        await self.jobs.execute("fail", [sys.executable, "-c", "raise SystemExit(7)"])
        self.assertEqual((await self.finished("fail"))["exit_code"], 7)
        await self.jobs.execute("timeout", [sys.executable, "-c", "import time; time.sleep(30)"], timeout=1)
        self.assertEqual((await self.finished("timeout"))["state"], "timed_out")

    async def test_output_limit(self):
        await self.jobs.execute("large", [sys.executable, "-c", "print('x'*200000)"])
        self.assertEqual((await self.finished("large"))["state"], "output_limit")

    async def test_cwd_escape(self):
        with self.assertRaises(ValueError):
            await self.jobs.execute("escape", ["pwd"], cwd="../")

    async def test_gateway_secret_not_inherited(self):
        import os
        os.environ["CLOUD_HAND_TOKEN"] = "test-secret"
        await self.jobs.execute("env", [sys.executable, "-c", "import os; print('CLOUD_HAND_TOKEN' in os.environ)"])
        self.assertIn("False", (await self.finished("env"))["output"])

if __name__ == "__main__":
    unittest.main()
