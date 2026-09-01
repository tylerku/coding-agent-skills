# Focused Review Dimensions

The gate asks whether the PR is unsafe to merge, not whether every aspect of the code is ideal.

## Logical correctness

Examine changed control flow, state transitions, data transformations, boundary conditions, error paths, null and empty cases, ordering, idempotency, concurrency, retries, time handling, and compatibility with directly affected callers and consumers.

Must-fix examples include reachable incorrect behavior, broken invariants, data corruption, unhandled required states, regression of stated behavior, and incompatible contract changes.

## Security

Examine authentication, authorization and ownership, input validation, injection boundaries, secrets, sensitive-data handling, privacy, unsafe rendering, rate limiting, path and network access, deserialization, dependency trust boundaries, and failure behavior.

Treat a demonstrated authorization bypass, credential exposure, injection path, unsafe sensitive-data disclosure, or explicit security-rule violation as must-fix. Do not block on generic hardening advice without a concrete changed-path risk.

## Architecture and style

Examine module boundaries, separation of concerns, dependency direction, cycles, public contracts, state ownership, data-access placement, framework conventions, types, names, control-flow clarity, comments, error handling, logging policy, file placement, and unnecessary complexity.

Style is must-fix only when it violates an explicit required project rule or creates a material correctness, safety, compatibility, operability, or maintainability failure. Cosmetic preferences and optional refactors are not gate findings. Treat invariant, ordering, compatibility, workaround, and safety comments as local contracts unless stronger current requirements supersede them.

## Test coverage

Examine whether tests cover the behavior introduced or changed, meaningful boundary and failure cases, regression risk, authorization and ownership boundaries, and high-risk state transitions. Verify that assertions exercise the intended path rather than merely executing code.

Do not use a numeric coverage percentage as the sole decision. Missing or ineffective tests are must-fix when the changed behavior is material and no adequate deterministic proof protects it; minor coverage opportunities are warnings or omitted.

## Documentation

First decide applicability. Documentation normally applies when the PR changes a public API, user-visible contract, configuration, setup, deployment or operational procedure, migration, data format, security expectation, or non-obvious maintainer contract.

Missing documentation is must-fix only when an explicit requirement demands it or omission would make the change unsafe, unusable, operationally hazardous, or materially misleading. Otherwise report a warning. Use `not_applicable` with a concrete reason when the change requires no documentation update.
