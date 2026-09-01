# Review Contract

Use this procedure when intended behavior or acceptance criteria are not already explicit and coherent.

## Required fields

- **Target:** the required open GitHub pull request, including repository, number, URL, full head SHA, head ref, and base ref.
- **Intent:** the observable outcome the change is supposed to create.
- **Acceptance criteria:** independently checkable behavior statements.
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

## Quality of acceptance criteria

Good criteria describe observable results and can be proven by a test, request, screenshot, database readback, or other concrete observation. Rewrite vague criteria as proposed interpretations, not authoritative facts.

When a missing decision changes product behavior, public API, storage, security posture, or owner boundary, mark behavioral conformance `blocked`. When evidence is merely unavailable in the environment, mark it `owed`.

The rest of the quality audit may proceed even when behavioral acceptance is blocked.

## Target evidence

Establish the reviewed change from exactly one matching open GitHub pull request and its authoritative diff. Record the repository, pull-request number and URL, full head SHA, head ref, base ref, and changed-file list. A path named in a request is scope, not proof that every file beneath it changed.

If the pull request or its diff cannot be established unambiguously, mark the review `blocked`, request a GitHub PR URL or number, and stop before specialist dispatch. Never fall back to local changes, a branch-only diff, a supplied patch, or an inferred whole-tree scope for this skill.
