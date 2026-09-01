# Performance and reliability

Review whether the change remains efficient and dependable under realistic load and failure.

## Examine

- Algorithmic complexity, repeated work, unbounded iteration, and growth with realistic input sizes.
- Database query count, N+1 behavior, indexes, query shape, pagination, transaction duration, locks, and contention.
- Network waterfalls, payload size, batching, caching, invalidation, compression, and duplicated requests.
- Client rendering frequency, expensive computations, bundle impact, images, layout work, and memory retention.
- Resource cleanup for timers, listeners, subscriptions, streams, handles, connections, and temporary files.
- Timeouts, retries, exponential backoff, jitter, circuit breaking, fallbacks, and prevention of retry storms.
- Idempotency, duplicate delivery, crash recovery, job leasing, at-least-once processing, and partial failure.
- Queues, concurrency limits, rate limits, backpressure, capacity, and graceful degradation.
- Logs, metrics, traces, health signals, and actionable failure context for new operational behavior.
- Behavior when dependencies are slow, unavailable, inconsistent, or return malformed data.

## Evidence standard

Prefer measurements, query plans, profiles, benchmarks, or load-aware tests. If measurement is unavailable, a finding must still identify a concrete hot path, realistic scale, and plausible cost or failure mechanism. Avoid unsupported claims that something is merely "slow" or "not scalable."
