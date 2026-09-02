---
name: smoke-test
description: Exercise the affected critical application journeys against a running test environment, capture screenshot and runtime evidence at each meaningful checkpoint, and optionally publish a standard report to a matching GitHub pull request. Use for smoke testing, UI journey proof, or screenshot-backed release confidence. Do not use as a source-code review or exhaustive acceptance-verification pass.
---

# Smoke Test

Prove that the affected critical journeys work in a running application. Report observed behavior from the exact code and environment tested; never infer a pass from source code or a green unit-test suite.

## Operating Contract

- Test and report only. Do not fix code, commit screenshots, merge, deploy, or change production data.
- A pull request is optional. When exactly one matching open pull request exists, an explicitly requested smoke test includes permission to create or update one canonical informational comment unless the user opts out. Otherwise keep all evidence in the session.
- Prefer local, ephemeral, preview, or staging environments with test accounts. Do not exercise a mutating journey against production or trigger real charges, messages, emails, bookings, or other external side effects without explicit authorization.
- Use one journey controller. Do not run browser agents concurrently against shared application state unless the project provides isolated accounts and data for each worker.
- Perform one bounded pass. A failed assertion may receive one diagnostic retry when the failure could be transient; do not loop, repair the implementation, or silently change the scenario.
- Screenshots prove rendered state, not behavior by themselves. Pair every checkpoint with an explicit observed assertion and inspect relevant browser-console and network failures.
- Do not claim exhaustive acceptance coverage. This skill proves the selected smoke journeys; a project acceptance-verification process may require additional criteria and evidence.

## 1. Freeze the Test Target

Record the repository, full commit SHA, branch, worktree state, environment, base URL, test-data source, and matching pull request when one exists. Inspect staged, unstaged, and untracked changes before testing.

For pull-request publication, require a clean worktree whose `HEAD` equals the pull-request head SHA. A dirty checkout may still be tested for local session feedback, but label the target `SHA + uncommitted changes`, include the changed-file inventory, and do not publish that evidence as proof of the pull request.

Start the application from the tested checkout on isolated ports and retain the process receipt. Reuse an existing server only when a deterministic mechanism proves that it serves the exact tested checkout and worktree state, such as a harness-owned process receipt or an application build identifier that matches the target. Port location, page appearance, or an assumed developer server is not provenance. If exact provenance cannot be established and an isolated instance cannot be started, report `blocked`.

Never kill an existing listener or assume an occupied port belongs to this run. Track and stop only processes started by this pass. If the target code or environment cannot be identified responsibly, report `blocked` before testing.

## 2. Resolve Project Guidance

Apply explicit user instructions first, followed by applicable `AGENTS.md` or `CLAUDE.md` files. Then look for `docs/smoke-test/smoke-test.yml` or `.yaml`.

If project smoke-test configuration exists, read [references/project-overrides.md](references/project-overrides.md). Project journeys and settings extend the global defaults unless `mode: replace` is explicit. Never load credentials from committed policy files; use the project's authorized secret or test-account mechanism.

## 3. Select the Journeys

Read [references/journey-selection.md](references/journey-selection.md). Select:

1. Every explicitly requested journey.
2. Configured `always` journeys applicable to the environment.
3. Critical happy paths directly affected by the task or pull-request diff.
4. The smallest adjacent journey needed to expose a broken integration boundary.

Do not expand a smoke pass into the entire regression suite. For each selected journey, state why it was selected, its actor and prerequisites, its start state, its ordered steps, its expected checkpoints, and its applicable viewports.

If intended behavior is too ambiguous to define an observable checkpoint, mark that journey `blocked`; do not invent the product decision.

## 4. Prepare a Safe Scenario

Use project-provided test accounts and synthetic or disposable data. Create only the minimum prerequisites needed and preserve unrelated developer data. Record material setup so another reviewer can understand the scenario.

Prefer the repository's existing browser or end-to-end harness. For web applications without one, use Playwright or another reproducible browser driver. Use semantic locators and observable state rather than sleeps. Wait on the condition that establishes readiness, with a finite timeout.

For responsive web UI without configured viewports, use:

- desktop: `1440x900`
- mobile: `390x844`

Apply both viewports to each visual journey unless the product or journey is genuinely single-viewport. Non-visual API or worker journeys use command, response, log, and persisted-state evidence; mark screenshots `not applicable` rather than fabricating them.

## 5. Execute and Capture Evidence

Read [references/evidence.md](references/evidence.md) before starting a visual journey.

For every selected journey and applicable viewport:

1. Establish the documented start state.
2. Execute each real user action in order.
3. After every meaningful step, assert the expected observable state and capture a screenshot of that checkpoint.
4. At the final state, confirm the journey outcome and any material persisted or downstream state that is within authorized reach.
5. Inspect unexpected browser-console errors and failed application requests. Record only failures relevant to the journey or disclose why they are unrelated.

Capture a failure screenshot at the point of failure. Preserve actual error text, response status, and the last successful checkpoint without exposing secrets or unnecessary personal data. Continue independent journeys when safe; stop dependent steps whose prerequisites failed.

## 6. Decide the Result

Use these states:

- `pass`: every selected journey passed every required checkpoint and viewport with sufficient evidence.
- `fail`: at least one expected behavior was observably wrong.
- `blocked`: required access, environment, test data, product decision, or evidence channel was unavailable.
- `stale`: the tested commit no longer matches the current pull-request head or declared target.

Do not convert a blocked journey into a pass because other journeys succeeded. Do not treat a relevant console exception or failed application request as harmless without evidence.

## 7. Report and Publish

Always return the complete session report defined in [references/output-contract.md](references/output-contract.md), including direct local artifact paths or available artifact links for every screenshot.

If a matching open pull request exists, the tested checkout was clean at its exact head SHA, and publication is authorized, read [references/pr-reporting.md](references/pr-reporting.md). Upload screenshots only through the project's authorized artifact mechanism. Never commit proof images merely to make them visible on a pull request, and never upload sensitive screenshots to a public location.

Immediately before publishing, re-fetch the pull request and compare its full head SHA with the frozen target. If it changed, do not publish stale evidence. Report `stale` and require a new run.
