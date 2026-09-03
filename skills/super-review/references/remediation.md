# Bounded Remediation

The review and repair phases have different responsibilities. Independent specialists find and adjudicate defects; one coordinated implementation pass repairs only accepted findings whose intended result is already established.

## Disposition

Assign every accepted blocker and warning exactly one disposition before editing:

- `auto_fix`: the defect is reachable, the required behavior is established by an explicit requirement or unambiguous compatibility invariant, the smallest fix is clear, the change remains within the PR's intent, and sufficient verification can run.
- `decision_required`: more than one materially different product, architecture, security, data, compatibility, rollout, or ownership choice could reasonably resolve the finding, or the authoritative requirement is missing or conflicting.
- `repair_owed`: the correct fix is clear but branch permission, environment, dependency access, or required verification prevents completing and pushing it safely.

Do not auto-fix an improvement unless the user explicitly includes improvements. Do not use confidence alone to decide repairability.

Examples that are normally `auto_fix` when supported by the repository contract include introduced type errors, missing error handling with established behavior, stale-cache invalidation, logger-policy violations, accessible labels, clearly missing regression tests, and direct violations of an explicit convention.

Examples that normally require a decision include competing rollout strategies, unresolved timezone or data ownership policy, public API compatibility choices without a declared migration contract, destructive schema changes, security-policy changes, and fixes that materially expand feature scope. A technically difficult fix may still be `auto_fix` when its required outcome is unambiguous; a small edit may still require a decision when it chooses behavior.

## Safe repair sequence

1. Confirm the PR remains open at the frozen initial head. Record the authoritative head repository owner/name as well as the head ref, and confirm that exact target is writable without force.
2. Prefer a clean isolated worktree or detached checkout at that exact SHA. Never mix repairs with unrelated local changes.
3. Implement all `auto_fix` findings in one coordinated wave, including focused tests and documentation required by those fixes.
4. Run the smallest authoritative focused checks for each repair, followed by broader checks required by the repository or affected surface.
5. If verification fails, allow one bounded diagnostic correction inside the same wave. If it still fails, mark the finding `open` or `repair_owed` and do not push a knowingly failing repair.
6. Re-fetch the PR head immediately before push. Push one ordinary commit to the exact head repository and head ref only when it still equals the initial SHA. For a fork PR, never mistake a same-named branch in the base repository for the contributor's head branch. Never force-push or overwrite an intervening update.
7. Confirm the PR head now equals the pushed repair commit, freeze it as the final SHA, and perform post-repair specialist verification.

When isolation is unavailable, use the existing checkout only if it is clean, exactly matches the PR head, and contains no unrelated user work. Record the chosen repair workspace and push target.

## Verification and lifecycle

Retain the original finding ID across every state:

- `fixed`: pushed final SHA contains the repair, authoritative checks pass, and the responsible specialist or adjudicator confirms the defect is resolved without an introduced material regression.
- `open`: the finding remains, the repair attempt failed, or the bounded wave exposed a new accepted defect.
- `decision_required`: no edit was made because a human decision is necessary.
- `repair_owed`: no complete pushed and verified repair was possible for an operational reason.

Record the first-seen SHA, original evidence, disposition reason, repair summary, repair commit when present, verification evidence, and final state. Fixed history remains visible in the canonical report so reviewers can distinguish a clean original review from a clean result achieved through remediation.
