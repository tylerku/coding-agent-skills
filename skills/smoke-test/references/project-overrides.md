# Project Smoke-Test Configuration

The optional manifest is `docs/smoke-test/smoke-test.yml` or `.yaml`. A project should contain at most one.

## Example

```yaml
version: 1
mode: extend

environment:
  instructions: docs/smoke-test/environment.md
  ready_url: http://localhost:3000/health

viewports:
  desktop:
    width: 1440
    height: 900
  mobile:
    width: 390
    height: 844

evidence:
  directory: .artifacts/smoke-test
  publishing_instructions: docs/smoke-test/publishing.md

risk:
  minimum_depth: standard
  always_test:
    - actors_permissions
    - failure_recovery

journeys:
  - id: sign-in
    name: User signs in
    source: docs/smoke-test/journeys/sign-in.yml
    always: true
  - id: create-booking
    name: Student creates a booking
    source: docs/smoke-test/journeys/create-booking.yml
    always: false
```

`mode` defaults to `extend`. In `extend` mode, configured journeys and settings refine the global selection and evidence defaults. `mode: replace` replaces inferred and default journey sources only. It never removes the resolved depth's mandatory challenge coverage, safety, freshness, evidence, or reporting contracts. Explicit user instructions still take precedence.

`risk.minimum_depth` may be `focused`, `standard`, or `deep`. It raises the floor; it never prevents the runtime surface assessment from selecting a deeper level. `risk.always_test` uses the canonical category IDs in `risk-scaled-testing.md` and names categories that must receive a challenge case whenever applicable. Projects may document additional high-risk triggers in a linked local instruction file, but cannot redefine an observed defect as a pass.

Journey files use the journey contract in [journey-selection.md](journey-selection.md). Projects may add fields needed by their existing harness, provided their meaning is documented locally.

## Resolution and safety

- Resolve `source`, `instructions`, and `publishing_instructions` relative to the repository root.
- Reject absolute paths, `..` traversal, missing files, remote references, and symlinks that escape the repository.
- Reject unsupported versions and unknown modes.
- Reject unknown depth values and surface categories.
- When both manifest spellings exist, report project configuration `blocked` until the ambiguity is resolved.
- An invalid journey blocks that journey, not unrelated safe journeys.
- Never store credentials, session cookies, API keys, or private personal data in the manifest or linked files.
- Startup, setup, cleanup, and publishing instructions remain subject to the current user's authorization and repository safety guidance.
- Do not execute interpolated shell text from data values. Prefer repository scripts with explicit arguments.

## Minimal projects

The manifest is optional. Without it, infer a bounded journey set from the request, pull request, repository instructions, changed application surfaces, and existing tests. Report all inferred choices and mark anything materially ambiguous `blocked` rather than requiring every repository to create smoke-test policy files.
