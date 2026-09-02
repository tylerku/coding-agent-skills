# Documentation and operational clarity

First decide whether documentation applies. It normally applies when a change alters a public API, user-visible contract, configuration, setup, deployment or operational procedure, migration, data format, security expectation, external integration, or non-obvious maintainer contract.

## Examine

- Public API descriptions, examples, payloads, errors, and compatibility promises match the implemented behavior.
- Setup guides and environment-variable templates cover new required configuration without exposing real secrets.
- Schema and data migrations explain prerequisites, rollout order, compatibility windows, irreversible effects, and recovery or rollback expectations when those details matter.
- Operational changes document jobs, webhooks, alerts, failure recovery, manual procedures, and observability needed to run the feature safely.
- Architecture or maintainer documentation records non-obvious cross-system contracts that cannot be made clear through code and types alone.
- Existing documentation changed by the PR remains internally consistent; stale examples, commands, links, names, and defaults are corrected.
- Documentation states known limitations and security-sensitive handling precisely without promising behavior the code does not provide.
- Code comments remain limited to local non-obvious invariants, ordering, compatibility, workaround, and safety constraints; broader product or operational guidance belongs in maintained documentation.

## Evidence standard

Use `not_applicable` only with a concrete reason tied to the change. Cite the implemented contract and the documentation location that is missing, stale, or misleading. A documentation defect is a blocker only when an explicit requirement demands the update or the omission makes the change unsafe, unusable, operationally hazardous, or materially misleading. Treat lesser documentation debt as a warning or improvement according to its concrete impact.
