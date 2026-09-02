---
name: smoke-test
description: Run a risk-scaled, adversarial smoke test of the full affected feature surface against a running application, including critical journeys, plausible edge cases, failure paths, and screenshot-backed evidence. Use for feature smoke testing, exploratory runtime validation, UI journey proof, or an attempt to find defects before release. Do not use as a source-code review or an exhaustive whole-product regression suite.
---

# Smoke Test

Challenge the full affected feature surface in a running application. Prove the intended journeys work and actively try to falsify the feature with proportionate edge cases and failure conditions. Report observed behavior from the exact code and environment tested; never infer a pass from source code or a green unit-test suite.

## Operating Contract

- Test and report only. Do not fix code, commit screenshots, merge, deploy, or change production data.
- A pull request is optional. When exactly one matching open pull request exists, an explicitly requested smoke test includes permission to create or update one canonical informational comment unless the user opts out. Otherwise keep all evidence in the session.
- Prefer local, ephemeral, preview, or staging environments with test accounts. Do not exercise a mutating journey against production or trigger real charges, messages, emails, bookings, or other external side effects without explicit authorization.
- Use one journey controller. Do not run browser agents concurrently against shared application state unless the project provides isolated accounts and data for each worker.
- Perform one bounded pass. A failed assertion may receive one diagnostic retry when the failure could be transient; do not loop, repair the implementation, or silently change the scenario.
- Screenshots prove rendered state, not behavior by themselves. Pair every checkpoint with an explicit observed assertion and inspect relevant browser-console and network failures.
- Scale breadth to the feature's actual surface and risk. A localized reversible UI behavior should stay focused; a provider migration, cross-system workflow, security boundary, communications path, payment path, data migration, webhook, or background-job change requires deeper testing.
- Do not claim exhaustive whole-product coverage. Cover the affected feature from every applicable angle, while a project acceptance-verification or regression process may still require additional criteria and unrelated journeys.

## 1. Freeze the Test Target

Record the repository, full commit SHA, branch, worktree state, environment, base URL, test-data source, and matching pull request when one exists. Inspect staged, unstaged, and untracked changes before testing.

For pull-request publication, require a clean worktree whose `HEAD` equals the pull-request head SHA. A dirty checkout may still be tested for local session feedback, but label the target `SHA + uncommitted changes`, include the changed-file inventory, and do not publish that evidence as proof of the pull request.

Start the application from the tested checkout on isolated ports and retain the process receipt. Reuse an existing server only when a deterministic mechanism proves that it serves the exact tested checkout and worktree state, such as a harness-owned process receipt or an application build identifier that matches the target. Port location, page appearance, or an assumed developer server is not provenance. If exact provenance cannot be established and an isolated instance cannot be started, report `blocked`.

Never kill an existing listener or assume an occupied port belongs to this run. Track and stop only processes started by this pass. If the target code or environment cannot be identified responsibly, report `blocked` before testing.

## 2. Resolve Project Guidance

Apply explicit user instructions first, followed by applicable `AGENTS.md` or `CLAUDE.md` files. Then look for `docs/smoke-test/smoke-test.yml` or `.yaml`.

If project smoke-test configuration exists, read [references/project-overrides.md](references/project-overrides.md). Project journeys and settings extend the global defaults unless `mode: replace` is explicit. Never load credentials from committed policy files; use the project's authorized secret or test-account mechanism.

## 3. Map the Feature Surface and Select Depth

Read [references/risk-scaled-testing.md](references/risk-scaled-testing.md). Before choosing cases, map the affected actors, roles, entry points, states, data, integrations, asynchronous paths, legacy behavior, and failure boundaries. Explicitly choose and report one depth:

- `focused`: localized, reversible behavior with a narrow surface and no material external or asynchronous boundary;
- `standard`: multiple states, layers, roles, persistence paths, or adjacent integrations;
- `deep`: provider or platform migration, security- or money-sensitive behavior, communications, webhooks, background jobs, data migration, cross-system state, irreversible effects, or broad compatibility risk.

Use the highest depth indicated by any material part of the change. A project may set a minimum depth, and an explicit user instruction may set or raise it. Never silently reduce depth because execution is inconvenient; report unavailable required evidence as `blocked`.

For `focused` depth, select the highest-value distinct challenges required by the focused contract; do not force one case per category. For `standard` and `deep`, identify at least one high-value challenge case for every applicable surface category. At every depth, prioritize realistic boundaries and failure mechanisms over combinatorial variations.

## 4. Select Journeys and Challenge Cases

Read [references/journey-selection.md](references/journey-selection.md). Select:

1. Every explicitly requested journey.
2. Configured `always` journeys applicable to the environment.
3. Critical happy paths directly affected by the task or pull-request diff.
4. Adjacent journeys needed to expose affected integration, persistence, compatibility, or lifecycle boundaries.
5. Risk-scaled edge cases and failure paths from the surface map.

Do not expand a smoke pass into unrelated regression coverage. For each selected journey or challenge case, state why it was selected, its actor and prerequisites, its start state, its ordered steps, its expected checkpoints, and its applicable evidence channels and viewports.

If intended behavior is too ambiguous to define an observable checkpoint, mark that journey `blocked`; do not invent the product decision.

## 5. Prepare a Safe Scenario

Use project-provided test accounts and synthetic or disposable data. Create only the minimum prerequisites needed and preserve unrelated developer data. Record material setup so another reviewer can understand the scenario.

Prefer the repository's existing browser or end-to-end harness. For web applications without one, use Playwright or another reproducible browser driver. Use semantic locators and observable state rather than sleeps. Wait on the condition that establishes readiness, with a finite timeout.

For responsive web UI without configured viewports, use:

- desktop: `1440x900`
- mobile: `390x844`

Apply both viewports to each visual journey unless the product or journey is genuinely single-viewport. Non-visual API or worker journeys use command, response, log, and persisted-state evidence; mark screenshots `not applicable` rather than fabricating them.

## 6. Execute and Capture Evidence

Read [references/evidence.md](references/evidence.md) before starting a visual journey.

For every selected journey and applicable viewport:

1. Establish the documented start state.
2. Execute each real user action in order.
3. After every meaningful step, assert the expected observable state and capture a screenshot of that checkpoint.
4. At the final state, confirm the journey outcome and any material persisted or downstream state that is within authorized reach.
5. Inspect unexpected browser-console errors and failed application requests. Record only failures relevant to the journey or disclose why they are unrelated.

For non-happy-path challenge cases, establish the boundary or failure condition through an authorized test mechanism, assert both the immediate behavior and recovery behavior, and verify that partial execution did not leave incorrect persisted or downstream state. Use external-provider sandboxes, test modes, fixtures, or supported fault injection; never damage a shared or production environment to manufacture a failure.

Capture a failure screenshot at the point of failure. Preserve actual error text, response status, and the last successful checkpoint without exposing secrets or unnecessary personal data. Continue independent journeys when safe; stop dependent steps whose prerequisites failed.

## 7. Decide the Result

Use these states:

- `pass`: every required journey and challenge case for the selected depth passed with sufficient evidence across every applicable surface category.
- `fail`: at least one expected behavior was observably wrong.
- `blocked`: required access, environment, test data, product decision, or evidence channel was unavailable.
- `stale`: the tested commit no longer matches the current pull-request head or declared target.

Do not convert a blocked journey or required challenge case into a pass because other cases succeeded. Do not treat a relevant console exception, failed application request, inconsistent persisted state, or recovery failure as harmless without evidence.

## 8. Report and Publish

Always return the complete session report defined in [references/output-contract.md](references/output-contract.md), including direct local artifact paths or available artifact links for every screenshot.

If a matching open pull request exists, the tested checkout was clean at its exact head SHA, and publication is authorized, read [references/pr-reporting.md](references/pr-reporting.md). Upload screenshots only through the project's authorized artifact mechanism. Never commit proof images merely to make them visible on a pull request, and never upload sensitive screenshots to a public location.

Immediately before publishing, re-fetch the pull request and compare its full head SHA with the frozen target. If it changed, do not publish stale evidence. Report `stale` and require a new run.
