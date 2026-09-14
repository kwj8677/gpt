# Cloud Hand 0.1.0 — implementation prototype

Independent Linux execution service. General ChatGPT chat is the controller.
No Work/Codex/LLM invocation is implemented. No dependency on the shop PC.
This directory is a standalone project; it does not change Local Codex Bridge.

## Current status
Source authored through GitHub API. Not runtime-tested or deployed.
The branch is a reviewable prototype, NOT a connected ChatGPT plugin.
There is no provisioned cloud host, public endpoint or verified ChatGPT connection.
No claim is made that ChatGPT will bill tool use against a particular allowance.

## Components
- Official MCP Python SDK v1 compatibility line; four tools on /mcp.
- Linux exact-argv subprocess executor, durable SQLite results, retry identity checking.
- One shell job at a time, bounded output, deadlines, process-group cleanup.
- Persistent Playwright Chromium browser, serial browser actions.
- Constant-time bearer authentication; no unauthenticated execution path.
- Loopback listener: deploy behind TLS and an OAuth-capable gateway supported by ChatGPT.
- No cloud credentials, user credentials, customer data or login cookies in source.

## Local verification on a Linux development host
```sh
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python -m playwright install --with-deps chromium
.venv/bin/python -m unittest -v test_jobs.py
.venv/bin/python -m compileall -q server.py jobs.py
```
Install dependencies in a disposable Linux environment. Version ranges must be
resolved, tested and locked before production. Run the service as a dedicated
unprivileged OS user with write access only to its data directory.
Set CLOUD_HAND_TOKEN through a secret manager to a random secret of >=32 characters.
Set CLOUD_HAND_ROOT to a persistent work directory and CLOUD_HAND_PUBLIC_HOST
to the actual gateway host (including port if nonstandard). Start server.py.
Never publish the bearer secret, expose an unauthenticated reverse proxy, mount
the Docker socket, or run this as host root.

## Connection contract
A compatible authenticated gateway forwards /mcp to 127.0.0.1:8765/mcp and sets
the backend bearer only AFTER validating the client's OAuth identity.
Gateway implementation and OAuth registration are still pending; the server
does not pretend to implement OAuth discovery, consent or token issuance.
Register that remote MCP URL through the supported ChatGPT plugin flow.
Plugin import/schema and iOS/general-Chat tool availability need live verification.

## Tools
hand_status(); hand_execute(request_id, argv, cwd, timeout);
hand_session(request_id, offset, cancel); hand_browser(action, url, selector, text).
Shell request IDs survive reconnects. An identical retry returns the original
job; a changed command using the same ID is rejected. Interrupted jobs are not
automatically replayed. Outputs are untrusted observations, never instructions.
Browser mutations do NOT have exactly-once delivery: after a timeout or disconnect,
observe the page before deciding whether to repeat the action.

## Known limitations / next gates
1. Execute tests; verify MCP initialize/list/call and unauthorized rejection.
2. Verify timeout/cancel descendant cleanup and container/service restart behavior.
3. Provision independent Linux host + persistent disk; implement compatible OAuth/TLS gateway.
4. Add secure operator browser login handoff before HandsOS/SmartPlace usage.
5. Validate ordinary Chat + iOS invocation, reconnect and actual usage accounting.
6. Verify target websites permit this cloud browser/IP; do not assume login portability.

One process/worker only. The executor is a powerful single-user tool, not a
multi-tenant sandbox. cwd validation is a default working-directory boundary,
not a restriction on what an authorized shell program can access.
Do not install model clients or add background autonomous AI.
Shell outputs persist in SQLite; retention/purge policy is not implemented yet.
Restart marks unfinished jobs interrupted; service supervisor must kill the old
process group/cgroup before restarting. No child process adoption is attempted.
Browser process failures currently require service restart. Browser screenshots
are returned as base64 JSON in this prototype; native image tool results are a
follow-up improvement. Password/OTP handoff and comprehensive DOM redaction
are not implemented: use only non-sensitive public-page tests until those gates pass.
