# Pull-Request Target Bootstrap

Use this only after confirming that no matching open pull request exists. The objective is to establish the durable review target, not to prepare unfinished work.

## Eligibility

Create one draft pull request only when all of these are true:

- The super review was explicitly requested and the user did not opt out of PR creation.
- The request targets the current change rather than an explicit PR URL or number that failed resolution. Never replace a missing, closed, or ineligible named PR with a new one.
- The working tree is clean, the checkout is on a named feature branch, and all intended review changes are already committed.
- The head branch is not a protected or base branch such as `main`, `master`, `dev`, a release branch, or another branch prohibited by repository policy.
- Repository identity, writable head repository and remote, head ref, and base repository are unambiguous.
- The base ref was already established and frozen through the main skill's precedence rule before PR discovery. Bootstrap may not reinterpret or replace it.
- The branch contains a non-empty coherent diff against the selected base and does not contain unrelated branch history that would make the PR misleading.
- A fresh host query confirms that no open PR uses that authoritative head repository/ref. An existing PR to another base is a base-target conflict, not permission to create a second PR; stop unless the user separately and explicitly resolves the existing PR situation.
- Existing authentication and permissions allow a normal push and draft-PR creation without installing tools, changing credentials, or bypassing policy.

If any condition fails, do not fall back to a local or inferred review. Return `blocked` with the exact missing prerequisite and smallest next action.

`report-only` disables review-triggered source repair; by itself it does not disable eligible draft-PR bootstrap or the canonical PR comment. The user may separately opt out of PR creation, in which case no-PR invocation stops as `blocked`.

## Safe sequence

1. Record local HEAD, branch, repository remotes, selected base, and the evidence that established the base.
2. Fetch current remote metadata without rewriting local history. Recheck that the base exists and the proposed diff is non-empty and coherent.
3. Query again for any open PR on the authoritative head repository/ref immediately before any push. Reuse one whose base matches; stop on a different-base conflict or ambiguous results.
4. If the exact remote head already equals local HEAD, do not push. If the remote head is absent or is an ancestor that accepts a normal fast-forward, push the current committed branch to that exact head repository/ref. Never force-push, rebase, rename the branch, or push to a same-named branch in a different repository.
5. Create one **draft** pull request against the frozen base. Derive a concise title and body from authoritative task context and the committed diff; identify it as the initial review target without claiming validation or completion.
6. Re-fetch the created PR and verify its open draft state, base repository/ref, authoritative head repository/ref, and full head SHA. Only then freeze the target and dispatch specialists.

Do not commit, stage, stash, discard, or otherwise alter dirty work to satisfy eligibility. Do not create an issue, branch, non-draft PR, label, assignment, milestone, or review request.

## Partial failure

Stop after one push attempt and one PR-creation attempt. If a push succeeds but PR creation fails, report the exact pushed repository/ref and creation error; do not retry with another base or repository. If PR creation returns an uncertain result, query by exact head repository/ref before doing anything else. Reuse exactly one result only when its base matches the frozen target; otherwise stop as `blocked`.
