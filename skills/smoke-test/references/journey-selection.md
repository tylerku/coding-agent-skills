# Journey Selection

A smoke test is a small, high-signal runtime check, not a full end-to-end regression suite. Select journeys that answer: "Could this change ship while a critical affected user path is obviously broken?"

## Evidence sources

Resolve journeys in this order:

1. Explicit user-requested journeys and viewports.
2. Project `docs/smoke-test/` configuration.
3. Pull-request description, linked issue, or supplied task acceptance criteria.
4. Changed routes, screens, API boundaries, jobs, and integrations.
5. Existing end-to-end tests and product documentation.
6. Clearly labeled inference from the diff and application structure.

Do not silently promote every acceptance criterion into a smoke journey. Acceptance verification may require exhaustive negative paths, detailed data assertions, performance measurements, or human judgment beyond smoke scope.

## Default selection rules

- Include a configured `always` journey when its platform and environment are available.
- Include the changed happy path from entry point to observable outcome.
- Include authentication or role transition only when it is part of reaching or exercising the changed behavior.
- Include one adjacent integration boundary when the change could appear successful in the UI while failing to persist or propagate.
- Include a high-risk negative checkpoint only when its failure would create an immediate security, money, data-loss, or access-control hazard. A comprehensive negative-path audit belongs elsewhere.
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
final_evidence:
  - UI, response, persisted row, emitted event, or other proof
```

Natural-language actions are acceptable when the runner can execute them reproducibly. Existing project test identifiers or helper names may be referenced. Never put passwords, tokens, or personal test-account details in the journey contract or report.

## Applicability

Record a concrete reason when a configured journey does not apply. Examples include a backend-only change with no user-facing flow, a mobile-only product, or an unavailable external sandbox. Do not run a specialist or browser merely to produce an obvious `not applicable` result.
