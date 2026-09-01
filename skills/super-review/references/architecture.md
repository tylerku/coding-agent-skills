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
- Migration, rollout, mixed-version, rollback, and feature-flag behavior where applicable.
- The project's documented architecture and approved exceptions.

## Evidence standard

Demonstrate the dependency or boundary violation and its concrete consequence. For circular dependencies, identify the actual cycle. Do not propose broad redesigns, speculative extensibility, or style preferences unrelated to the reviewed change.
