# Code quality and conventions

Review whether the implementation is the simplest clear expression of the required behavior and follows the repository's conventions.

## Examine

- Names communicate domain intent and distinguish concepts that have different invariants or lifecycles.
- Functions, components, modules, and types remain focused and appropriately sized for the project.
- Control flow is readable; compound conditions, nesting, mutation, and early exits make intent clear.
- Duplication is removed when it represents one concept, but unrelated code is not forced behind a premature abstraction.
- Types make invalid states difficult to represent; casts, broad types, nullability, and unchecked assumptions are justified.
- Comments explain only non-obvious reasons or constraints and do not restate the code.
- Existing invariant, ordering, compatibility, workaround, and safety comments are treated as local contracts. Verify that the change still satisfies them, or that a stronger current requirement explicitly supersedes them.
- Dead code, debug scaffolding, commented-out code, accidental generated artifacts, and unrelated churn are absent.
- Errors are handled at the right layer with useful context and without being swallowed or duplicated.
- Logging uses the project's dedicated logging abstraction when one exists or is required. Prefer structured context, intentional levels, and redaction. Flag direct `console.log`, `console.error`, raw stdout/stderr, or equivalent calls when they bypass that policy.
- Formatting, file placement, imports, exports, naming patterns, and framework idioms match local precedent.
- The implementation avoids unnecessary indirection, configuration, dependencies, and cleverness.

## Evidence standard

The project defines its exact conventions and logger APIs. Cite the local rule or established pattern when possible. Tie a finding to readability, maintainability, diagnosability, or defect risk; do not request cosmetic churn with no material benefit.
