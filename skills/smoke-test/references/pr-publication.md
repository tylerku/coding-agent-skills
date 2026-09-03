# Pull-Request Publication

The canonical body comes exclusively from [report-contract.md](report-contract.md). This file defines publication mechanics only; it does not define a second summary or template.

Publish only from a clean checkout whose `HEAD` is the exact open pull-request head SHA and whose running application has deterministic provenance to that checkout. A dirty-worktree run remains session-only even when its base commit equals the pull-request head.

## Comment identity and migration

Prepend this marker to the canonical report:

```html
<!-- smoke-test-report:v3 -->
```

Search first for the v3 marker. For migration, also search comments owned by the active reviewer identity for:

```html
<!-- smoke-test-report:v2 -->
<!-- smoke-test-report:v1 -->
```

Update one owned older comment in place. Never edit another author's marked comment or append a new comment on every rerun.

## Screenshot publication

Upload every visual checkpoint through the project's authorized artifact mechanism and confirm that each URL is accessible to intended reviewers before publishing. Substitute the confirmed URL for the session artifact path while preserving the same checkpoint ID, image, caption, order, expected result, observed result, and state.

Never commit proof images merely to make them visible on a pull request. Never upload sensitive screenshots to an unauthorized or public location. When any required image cannot be safely published, retain its canonical checkpoint, record the limitation, and set pull-request publication to `OWED`; preserve the complete session report and images. Session delivery independently uses `DELIVERED` or `OWED` as defined by the canonical contract.

## Freshness

Immediately before writing, re-fetch the pull request. If its repository, number, open state, head ref, base ref, or full head SHA differs from the frozen target, publish nothing. Set the overall result to `STALE`, the pull-request publication state to `WITHHELD_STALE`, and report both SHAs in the canonical limitations section.

After writing, record the pull-request comment URL and `CREATED` or `UPDATED` state in the session rendering of the same report model.
