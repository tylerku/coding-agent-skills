# Architecture and compatibility

Review whether the change fits the system's intended boundaries and remains evolvable without imposing personal architectural taste.

## Examine

- Dependency direction, layer boundaries, import cycles, and runtime cycles.
- Separation among presentation or transport, domain logic, persistence, and external integrations.
- Clear ownership of state, invariants, validation, orchestration, and side effects.
- Coupling, cohesion, shared mutable state, and hidden temporal ordering.
- Compatibility of public APIs, schemas, events, storage formats, configuration, and protocols.
- Whether an abstraction removes meaningful duplication or instead hides a simple local operation.
- Duplicate sources of truth or parallel implementations that can drift.
- Necessity of every added schema column, persisted field, model property, public API method, export, and configuration key. Each needs a reader or a documented consumer in the change or an authoritative plan. Flag one that is only written, or that duplicates state already recorded elsewhere (for example a timestamp a related row already holds).
- Migration, rollout, mixed-version, rollback, and feature-flag behavior where applicable.
- The project's documented architecture and approved exceptions.

## Evidence standard

Demonstrate the dependency or boundary violation and its concrete consequence. For circular dependencies, identify the actual cycle. Do not propose broad redesigns, speculative extensibility, or style preferences unrelated to the reviewed change.

## Project boundary conformance

For changed code crossing a documented layer boundary, record the applicable rule, the functions examined, where business decisions and persistence execute, and any claimed exception in `evidence` and `scope_examined`. Inspect function bodies and relevant callees; directory names and valid imports alone do not establish separation. Cover every changed boundary operation, grouping operations only when the same verified mechanism applies. Mark missing required source evidence `owed` rather than inferring a pass.

When atomicity is offered as a reason for placing business logic in persistence, inspect the project's transaction or unit-of-work mechanism first. Trace whether the intended owner can execute its rules through data-access objects sharing one transaction client. Verify participating reads/writes use that client, required failures propagate to rollback, and concurrency-sensitive invariants retain their locks or conditional checks. A transaction wrapper alone does not justify moving policy into persistence; an exception for atomic database operations does not automatically cover business decisions.

Classify an added persisted column or field that nothing reads, or that duplicates existing state, as at least `warning`: once released, schema is costly to remove. Show the writes and the absence of readers. A builder choice in the contract does not exempt it.

Classify a verified, in-scope violation of a mandatory project layer rule as at least `warning`, even when tests pass and no runtime bug is demonstrated. Cite the exact rule and code; explain the misplaced responsibility and maintenance or correctness consequence. Reserve `improvement` for optional design refinements that satisfy applicable rules. An explicit approved exception or superseding instruction must be cited and shown to apply. Repair difficulty or the need for authorization changes repair disposition, not severity.
