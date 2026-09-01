# Test comprehensiveness

Review whether the test suite would reliably detect material regressions introduced by the change.

## Examine

- Map each acceptance criterion and important behavior branch to existing or newly added evidence.
- Cover happy paths, boundaries, invalid inputs, authorization failures, recovery paths, and meaningful empty states.
- Cover concurrency, idempotency, retries, timeouts, partial failures, and duplicate events when the implementation permits them.
- Verify persistence, emitted events, external calls, cache changes, and other side effects rather than only return values.
- Add or identify a regression test for the underlying bug class, not just the single reported example.
- Check that assertions prove observable outcomes rather than implementation details.
- Check mock fidelity: mocks must preserve the contracts and failure modes that matter.
- Check isolation, deterministic setup, cleanup, ordering independence, and likely sources of flakiness.
- Use the narrowest test level that proves the contract, while retaining integration or end-to-end coverage where boundaries are the risk.
- Treat screenshots, typechecks, static analysis, and coverage reports as distinct evidence; none substitutes automatically for behavioral tests.

## Evidence standard

Coverage percentage is not proof of completeness. Name the untested behavior and the regression it could allow. Do not demand tests for trivial declarations, generated code, or behavior already proven more effectively at another level.
