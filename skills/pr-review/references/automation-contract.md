# GitHub Automation Contract

The skill defines the gate decision. A surrounding GitHub workflow, webhook service, or autonomous pipeline must invoke it and publish the result.

## Recommended events

Run on pull-request `opened`, `synchronize`, `reopened`, and `ready_for_review`. Group runs by repository and PR number, cancel an in-progress run when a newer SHA arrives, and require a fresh result for the current head SHA.

Use the required check name:

```text
PR Review / Must-Fix Gate
```

Configure a GitHub ruleset or branch-protection rule to require that check. A failed check is only advisory until repository merge policy requires it.

## Canonical comment

When comment publication is authorized, create or update one comment owned by the active reviewer identity with this marker as its first line:

```html
<!-- pr-review-report:v2 -->
```

Search first for the v2 marker. For migration, also search for `<!-- pr-review-report:v1 -->`. Update an owned older comment in place; never edit another author's marked comment or append a new comment on every rerun.

Use this fixed order:

```markdown
<!-- pr-review-report:v2 -->
## PR Must-Fix Gate

| Gate | Reviewed commit | Reviewed at |
| --- | --- | --- |
| **{{PASS_OR_FAIL_OR_BLOCKED}}** | [`{{short_sha}}`]({{full_sha_url}}) | `{{utc_iso8601}}` |

### Must fix

{{must_fix_entries_or_none}}

### Warnings

{{warning_entries_or_none}}

### Coverage

| Dimension | State | Summary |
| --- | --- | --- |
| Logical correctness | {{state}} | {{summary}} |
| Security | {{state}} | {{summary}} |
| Architecture and style | {{state}} | {{summary}} |
| Test coverage | {{state}} | {{summary}} |
| Documentation | {{state}} | {{summary}} |

### Policy sources

{{effective_policy_sources_or_none}}

### Limitations

{{limitations_or_none}}

> This is a focused must-fix gate, not a comprehensive quality audit. Invoke `super-review` separately for exhaustive review.
```

Use `None.` for empty sections. Findings use stable IDs, confidence percentages, the concrete impact, smallest fix, and immutable full-SHA line links. Re-fetch the PR immediately before writing; never publish a result for a stale SHA.
