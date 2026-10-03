# Correctness and regressions

Review whether the change behaves correctly across every affected path, not only the happy path.

## Examine

- Trace each acceptance criterion through the actual entry points, branches, state transitions, persistence, and externally visible effects.
- Exercise valid, invalid, empty, null, duplicate, boundary, partial, and out-of-order inputs where applicable.
- Inspect asynchronous behavior: races, stale state, cancellation, retries, timeouts, reentrancy, and duplicate delivery.
- Check transactions and multi-step operations for partial failure, rollback, atomicity, and idempotency.
- Check dates, time zones, locale, ordering, rounding, overflow, units, and numeric precision when relevant.
- Follow errors through propagation, user-visible recovery, cleanup, and retry behavior.
- Check compatibility with existing callers, stored data, APIs, events, jobs, caches, feature flags, and configuration.
- Verify cache invalidation and consistency of derived or duplicated state.
- Confirm unchanged behavior remains unchanged outside the requested scope.
- When the change introduces an invariant that existing code must respect, such as a shared resource, a new state, or a new ownership rule, inventory every existing path that reads or writes the affected entities or external resources. Classify each as safe, guarded (cite the guard), or needing a fix. Do not sample a few callers; an uninventoried path is the most likely source of the next regression.

## Evidence standard

Prefer a reproducer, focused test, trace, or direct path analysis. A finding must name the triggering state or input and the incorrect observable outcome. Do not report a hypothetical edge case unless the code can actually reach it.
