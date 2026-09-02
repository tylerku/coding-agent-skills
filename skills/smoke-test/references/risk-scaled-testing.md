# Risk-Scaled Feature Challenge

The goal is not merely to demonstrate the expected path. Build the strongest proportionate case that the affected feature survives realistic use, misuse, boundary conditions, and dependency failures. Actively try to find a defect.

## Map the affected surface

Assess every category and record `applicable` or a concrete reason for `not applicable`:

| ID | Category | Questions |
| --- | --- | --- |
| `actors_permissions` | Actors and permissions | Which roles, ownership boundaries, account states, tenants, or unauthenticated callers can reach it? |
| `entry_points` | Entry points | Which UI routes, APIs, webhooks, jobs, commands, devices, or provider callbacks enter the feature? |
| `inputs_boundaries` | Inputs and boundaries | What happens for empty, invalid, maximum, minimum, duplicate, internationalized, stale, or unexpected values? |
| `state_lifecycle` | State and lifecycle | Which initial, loading, empty, partial, completed, cancelled, expired, disabled, migrated, or deleted states matter? |
| `persistence_consistency` | Persistence and consistency | Does the result persist, reload, synchronize, roll back, and agree across UI, API, database, cache, and downstream systems? |
| `timing_repetition` | Timing and repetition | What happens under rapid actions, retries, duplicates, concurrent changes, delayed responses, or out-of-order events? |
| `integrations_async` | Integrations and async work | Which external providers, queues, webhooks, scheduled jobs, credentials, rate limits, and delivery states participate? |
| `failure_recovery` | Failure and recovery | What happens on validation failure, timeout, provider rejection, partial success, network loss, restart, or dependency outage? |
| `compatibility_rollout` | Compatibility and rollout | Must old data, legacy providers, existing sessions, feature flags, rollback, or mixed-version behavior still work? |
| `presentation_platform` | Presentation and platform | Which responsive sizes, browsers, accessibility interactions, loading states, and user-visible error states matter? |
| `side_effects_observability` | Side effects and observability | Could it double-send, double-charge, lose data, leak information, or fail without the expected log, metric, or audit signal? |

The map covers the affected feature, not the whole product. Trace one boundary beyond the changed code whenever that boundary can hide a false success.

At `focused` depth, map every category for visibility but challenge only the highest-value subset required below. At `standard` and `deep`, challenge every applicable category.

## Select test depth

### Focused

Use when the change is localized, reversible, single-role, and has no material provider, schema, background-job, or security boundary.

Required coverage:

- the primary intended journey;
- persistence and reload when the feature writes state;
- the two highest-value distinct edge or failure cases when two plausible cases exist;
- relevant desktop and mobile presentation.

Example: an autosave behavior might challenge rapid successive edits, a failed save followed by recovery, navigation before completion, and reload consistency. Select only the cases applicable to the implementation rather than running a generic checklist blindly.

### Standard

Use when the change crosses UI/API/data layers, supports multiple roles or lifecycle states, changes durable data, or affects an adjacent integration.

Required coverage:

- every affected critical journey and actor;
- a representative challenge for each applicable surface category;
- authorization and ownership boundaries when data is scoped;
- persistence, reload, retry, duplicate-action, partial-failure, and recovery behavior when applicable;
- the most likely adjacent regression path.

### Deep

Use when any material part involves an external-provider migration, communications, authentication, authorization, payments, webhooks, queues, background jobs, data migration, concurrency, irreversible effects, or broad compatibility and rollout risk.

Required coverage:

- all affected actors, entry points, lifecycle states, integration directions, and downstream outcomes;
- representative valid, invalid, boundary, duplicate, delayed, out-of-order, timeout, rejection, partial-success, and recovery cases wherever applicable;
- retry safety and idempotency for repeatable or asynchronous operations;
- legacy-data, coexistence, cutover, rollback, and mixed-state behavior for migrations;
- provider sandbox or test-mode evidence, persisted state, user-visible state, and expected operational signals;
- a disclosed matrix of untestable cases; any required high-risk case without evidence prevents `pass`.

A communications-provider migration is deep because the visible UI may succeed while inbound handling, outbound delivery, callback verification, duplicate or out-of-order status events, retry behavior, number formats, rate limits, provider outages, legacy records, or operational visibility fail independently.

## Choose challenge cases

For each applicable category, ask:

1. What is most likely to break because of this change?
2. What failure would be most damaging or hardest to notice?
3. What assumption is the implementation relying on?
4. Which boundary could make the UI appear successful while the system is wrong?
5. Which repeated, delayed, partial, or unauthorized action could produce a different result?

Select the smallest set that meaningfully challenges those hypotheses. Do not spend the pass enumerating equivalent strings or permutations while a more important state, permission, retry, or integration boundary remains untested.

## Evidence standard

A challenge case passes only when its expected behavior is observed through the channels that establish correctness. Depending on the surface, that can require the user-visible result, API or provider receipt, persisted state, downstream event, and recovery state to agree.

If a test double proves only local handling but the real provider sandbox is required to establish the contract, label that limitation. Never equate mocked success with end-to-end provider proof.
