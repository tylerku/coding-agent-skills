# Session Output Contract

Report in this order.

## 1. Result

State `PASS`, `FAIL`, `BLOCKED`, or `STALE` and summarize the most important observed outcome in one sentence.

## 2. Test receipt

| Field | Value |
| --- | --- |
| Repository | owner/name or local path |
| Commit | full SHA |
| Worktree | clean, or dirty with changed-file inventory |
| Pull request | URL or `None` |
| Environment | local, preview, staging, or other |
| Base URL | redacted when necessary |
| Server provenance | process receipt or matching build identity |
| Run at | UTC ISO-8601 |
| Harness | Playwright, project runner, API client, or other |
| Policy sources | explicit request and project files used |

## 3. Journey summary

| Journey | Selection reason | Viewports | State | Last checkpoint |
| --- | --- | --- | --- | --- |

Use journey states `pass`, `fail`, `blocked`, or `not_applicable`.

## 4. Checkpoint evidence

For each journey, list checkpoints in execution order:

```text
1. Entry state — PASS
   Action: Navigated to the booking form as a student.
   Expected: Available session details and enabled Continue button.
   Observed: Expected form rendered and Continue was enabled.
   Evidence: /absolute/path/or/authorized-url.png
   Runtime: No relevant console errors or failed requests.
```

Embed or attach images in the session when the host supports it. Otherwise provide direct artifact paths or authorized links. Include failure evidence at the failed checkpoint.

## 5. Runtime observations

List relevant console exceptions, failed application requests, persisted-state checks, diagnostic retries, and known baseline noise. Use `None.` when empty.

## 6. Limitations and next action

Identify anything not exercised, evidence that could not be published, environmental constraints, and the smallest next action. Never imply that unselected journeys passed.

## 7. Publication

State whether the canonical pull-request comment was `created`, `updated`, `not_applicable`, `owed`, or withheld because the result was `stale`.
