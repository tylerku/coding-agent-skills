# Review Contract

Use this procedure when intended behavior or acceptance criteria are not already explicit and coherent.

## Required fields

- **Target:** the required resolved or safely bootstrapped open GitHub pull request, including base repository, number, URL, authoritative head repository owner/name, full head SHA, head ref, and base ref.
- **Intent:** the observable outcome the change is supposed to create.
- **Acceptance criteria:** independently checkable behavior statements that come from an owner decision or another authoritative source.
- **Builder choices:** implementation details the builder, an agent, or an agent-written plan chose without owner approval, such as new columns, fields, methods, exports, configuration, and plan specifics. They are not acceptance criteria.
- **Out of scope:** explicit boundaries and deliberately deferred work.
- **Affected surfaces:** components, APIs, data, jobs, integrations, and users.
- **Risk:** low, medium, high, or critical, with reasons.
- **Evidence sources:** task/issue, conversation, PR, docs, tests, and observed behavior.
- **Inferences:** assumptions not stated by an authoritative source.

## Source precedence

Prefer explicit task authority over inference:

1. Current user request and explicit decisions.
2. Pinned task or issue description.
3. PR description when it is consistent with the task.
4. Applicable repository instructions and specifications.
5. Existing tests and behavior as evidence of compatibility expectations.

Do not borrow criteria from a similar-looking task. Do not treat a filename hint as an exhaustive implementation boundary.

## Owner decisions versus builder choices

A plan or PR description written by the builder or an agent is not owner authority for its implementation details. Record a detail as an acceptance criterion only when the owner decided it or an authoritative source requires it. List every other detail under builder choices, and tell specialists to challenge whether each is needed. Never present a builder choice as a requirement to verify. A persisted field that nothing reads can otherwise pass review because the contract said to add it.

## Quality of acceptance criteria

Good criteria describe observable results and can be proven by a test, request, screenshot, database readback, or other concrete observation. Rewrite vague criteria as proposed interpretations, not authoritative facts.

When a missing decision changes product behavior, public API, storage, security posture, or owner boundary, mark behavioral conformance `blocked`. When evidence is merely unavailable in the environment, mark it `owed`.

The rest of the quality audit may proceed even when behavioral acceptance is blocked.

## Target evidence

Establish the reviewed change from exactly one matching open GitHub pull request and its authoritative diff. The pull request may have existed before the run or been safely created under `pr-target.md`; no specialist work begins before it exists and is verified. Record the base repository, pull-request number and URL, authoritative head repository owner/name, full head SHA, head ref, base ref, and changed-file list. A path named in a request is scope, not proof that every file beneath it changed.

If the pull request or its diff cannot be established unambiguously after eligible bootstrap, mark the review `blocked`, report the missing prerequisite, and stop before specialist dispatch. Never fall back to local changes, a branch-only diff, a supplied patch, or an inferred whole-tree scope for this skill.
