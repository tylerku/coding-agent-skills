# Pull-Request Reporting

Publish only from a clean checkout whose `HEAD` is the exact open pull-request head SHA and whose running application has deterministic provenance to that checkout. A dirty-worktree run remains session-only even when its base commit equals the pull-request head. Upload screenshots first through a project-authorized artifact mechanism, confirm that every published link is accessible to intended reviewers, then create or update exactly one informational comment owned by the active identity.

Use this marker as the first line:

```html
<!-- smoke-test-report:v1 -->
```

Do not edit another author's marked comment. Do not append a new comment on every rerun.

Use this fixed structure:

```markdown
<!-- smoke-test-report:v1 -->
## Smoke Test

| Result | Tested commit | Environment | Tested at |
| --- | --- | --- | --- |
| **{{PASS_OR_FAIL_OR_BLOCKED}}** | [`{{short_sha}}`]({{full_sha_url}}) | {{environment}} | `{{utc_iso8601}}` |

### Journey summary

| Journey | Viewports | State | Last checkpoint |
| --- | --- | --- | --- |
| {{journey}} | {{viewports}} | {{state}} | {{checkpoint}} |

### Checkpoint evidence

#### {{journey_name}} — {{viewport}}

1. **{{checkpoint}} — {{state}}**  
   {{observed_summary}}  
   ![{{journey_id}} {{viewport}} {{checkpoint}}]({{authorized_artifact_url}})

### Runtime observations

{{console_network_and_persistence_observations_or_none}}

### Limitations

{{limitations_or_none}}

> This report proves only the selected runtime smoke journeys. It is not a source-code review or exhaustive acceptance verification.
```

Use `None.` for empty sections. Include all meaningful checkpoint images in execution order, not only the final successful screen. When an artifact cannot be safely uploaded, say so in `Limitations`, preserve its local path in the session report, and mark publication `owed`; never substitute a source-control commit or an unauthorized public upload.

Immediately before writing, re-fetch the pull request. If its repository, number, open state, head ref, base ref, or full head SHA differs from the frozen target, publish nothing and return `stale` with both SHAs.
