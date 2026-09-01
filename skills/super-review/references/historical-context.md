# Historical Context Review

Run this cross-cutting specialist in parallel with the applicable quality-dimension specialists. It supplies evidence and candidate findings to those dimensions; it does not create an additional final matrix dimension.

## Examine

- Git blame and focused history for changed lines and adjacent invariants.
- Commit messages and diffs that explain why the affected behavior or structure exists.
- Earlier pull requests touching the same files or contracts, including unresolved or recurring review comments when accessible.
- Relevant linked issues, regressions, reversions, and compatibility decisions.
- Existing invariant, ordering, compatibility, workaround, and safety comments in the changed and directly affected code.

## Evidence rules

- Use history to recover intent and risk, not to preserve obsolete behavior automatically.
- Current explicit requirements override historical preferences.
- Cite the commit, pull request, issue, comment, or code location supporting each conclusion.
- Tie candidate findings to a defect introduced or exposed by the current pull request. Record unrelated historical debt only as a follow-up when it materially affects risk.
- If history is shallow, unavailable, or contains no relevant evidence, say so plainly; do not invent intent.
