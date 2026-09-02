# Pull-Request Reporting

Publish only from a clean checkout whose `HEAD` is the exact open pull-request head SHA and whose running application has deterministic provenance to that checkout. A dirty-worktree run remains session-only even when its base commit equals the pull-request head. Upload screenshots first through a project-authorized artifact mechanism, confirm that every published link is accessible to intended reviewers, then create or update exactly one informational comment owned by the active identity.

Use this marker as the first line:

```html
<!-- smoke-test-report:v2 -->
```

Search first for the v2 marker. For migration, also search for `<!-- smoke-test-report:v1 -->`. Update an owned older comment in place. Do not edit another author's marked comment or append a new comment on every rerun.

Use this fixed structure:

```markdown
<!-- smoke-test-report:v2 -->
## Smoke Test

| Result | Tested commit | Depth | Environment | Tested at |
| --- | --- | --- | --- | --- |
| **{{PASS_OR_FAIL_OR_BLOCKED}}** | [`{{short_sha}}`]({{full_sha_url}}) | {{focused_standard_or_deep}} | {{environment}} | `{{utc_iso8601}}` |

### Feature surface

| Category | Applicability | Challenge result |
| --- | --- | --- |
| {{category}} | {{applicability}} | {{result_or_reason}} |

### Journey and challenge summary

| Case | Type | Surface | Evidence | State |
| --- | --- | --- | --- | --- |
| {{case}} | {{journey_or_challenge}} | {{surface_category}} | {{evidence_channels}} | {{state}} |

### Checkpoint evidence

#### {{journey_name}} — {{viewport}}

1. **{{checkpoint}} — {{state}}**  
   {{observed_summary}}  
   ![{{journey_id}} {{viewport}} {{checkpoint}}]({{authorized_artifact_url}})

### Runtime observations

{{console_network_and_persistence_observations_or_none}}

### Defects found

{{observed_defects_or_none}}

### Limitations

{{limitations_or_none}}

> This is a risk-scaled runtime challenge of the affected feature, not a source-code review or unrelated whole-product regression suite.
```

Use `None.` for empty sections. Include all meaningful checkpoint images in execution order, not only the final successful screen. When an artifact cannot be safely uploaded, say so in `Limitations`, preserve its local path in the session report, and mark publication `owed`; never substitute a source-control commit or an unauthorized public upload.

Immediately before writing, re-fetch the pull request. If its repository, number, open state, head ref, base ref, or full head SHA differs from the frozen target, publish nothing and return `stale` with both SHAs.
