# Journey Selection

A smoke test is a high-signal runtime challenge whose breadth scales with the affected feature. Select journeys and edge cases that answer: "How could this feature be wrong even if its obvious happy path appears to work?"

## Evidence sources

Resolve journeys in this order:

1. Explicit user-requested journeys and viewports.
2. Project `docs/smoke-test/` configuration.
3. Pull-request description, linked issue, or supplied task acceptance criteria.
4. Changed routes, screens, API boundaries, jobs, and integrations.
5. Existing end-to-end tests and product documentation.
6. Clearly labeled inference from the diff and application structure.

Do not silently promote every unrelated acceptance criterion into a smoke journey. Do include criteria, edge cases, and failure paths that materially exercise the affected feature surface at the selected depth.

## Default selection rules

- Include a configured `always` journey when its platform and environment are available.
- Include the changed happy path from entry point to observable outcome.
- Include authentication or role transition only when it is part of reaching or exercising the changed behavior.
- Include every affected integration boundary needed to catch a false success at the selected depth.
- Include representative invalid, boundary, repeat, partial-failure, degraded, and recovery cases from the feature surface map.
- Include security, money, communications, data-loss, privacy, and access-control challenge cases whenever those consequences are plausible.
- Exclude unrelated product tours and cosmetic states that do not affect the changed journey.

## Journey contract

Before execution, define:

```yaml
id: stable-short-id
name: Human-readable journey
selection_reason: Why this path is in this pass
actor: Test role or unauthenticated
prerequisites:
  - Required safe test state
viewports:
  - desktop
  - mobile
steps:
  - action: Observable user action
    expect: Observable resulting state
    screenshot: short-checkpoint-name
challenge:
  category: failure_recovery
  hypothesis: The state may appear saved after the request fails
final_evidence:
  - UI, response, persisted row, emitted event, or other proof
```

Natural-language actions are acceptable when the runner can execute them reproducibly. Existing project test identifiers or helper names may be referenced. Never put passwords, tokens, or personal test-account details in the journey contract or report.

## Applicability

Record a concrete reason when a configured journey does not apply. Examples include a backend-only change with no user-facing flow, a mobile-only product, or an unavailable external sandbox. Do not run a specialist or browser merely to produce an obvious `not applicable` result.
