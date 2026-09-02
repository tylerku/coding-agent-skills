# Pull-Request Reporting

Always return the complete review in the active session. Pull-request publication mirrors that result; it is not the only copy.

## Discovery and authorization

- Resolve exactly one matching open GitHub pull request from the frozen repository, head ref or commit, and expected base. Never review or post to a title match or a merely similar branch.
- A matching GitHub pull request is a prerequisite for the review, not merely an optional reporting destination. Draft pull requests remain eligible unless project policy says otherwise.
- Never push, create a branch, or create a pull request to obtain a reporting destination.
- An explicitly requested super-review authorizes updating the canonical informational comment unless the user opts out. If invocation was implicit, repository ownership is unclear, or the host requires confirmation, ask immediately before the write.
- Honor project instructions and code-host permissions. Do not install a CLI or authenticate a new account without authorization.

## Canonical comment

Use exactly one comment containing this marker as its first line:

```html
<!-- super-review-report:v3 -->
```

Search first for the v3 marker. For migration, also search for `<!-- super-review-report:v2 -->` and `<!-- super-review-report:v1 -->`. Update an existing marked comment only when it is owned by the active reviewer identity; replace an owned older comment in place with the v3 structure and marker. Otherwise create one new v3 comment. Never edit another author's marked comment and never append a fresh comment on every rerun.

## Fixed rendering contract

Render the following structure exactly. Do not rename, reorder, or omit sections. Use `None.` for an empty finding or note group. Keep the conclusion to at most two sentences and keep table summaries to one concise sentence.

Allowed values:

- Overall state: `PASS`, `FINDINGS`, `OWED`, `BLOCKED`.
- Dimension state: `PASS`, `FINDINGS`, `NOT_APPLICABLE`, `OWED`, `BLOCKED`.
- Check result: `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`.
- Adjudication state: `COMPLETED`, `NOT_REQUIRED`, `OWED`.

Apply these formatting rules on every run:

- Compute overall state with this precedence: `BLOCKED`, then `OWED`, then `FINDINGS`, then `PASS`.
- Use the first 12 characters of the reviewed SHA for `short_sha`, while every URL contains the full SHA.
- Use a UTC timestamp formatted as `YYYY-MM-DDTHH:MM:SSZ`.
- Keep the eight dimension rows in the displayed order below.
- Sort findings by stable finding ID within each severity section.
- List deterministic checks in execution order and reviewer roles in workflow order.
- Escape pipe characters and collapse newlines inside table cells so Markdown tables remain valid.
- Do not add emojis, badges, extra headings, generated-by signatures, or prose outside the template.

````markdown
<!-- super-review-report:v3 -->
## Super Review

| State | Reviewed commit | Base | Profile | Reviewed at |
| --- | --- | --- | --- | --- |
| **{{overall_state}}** | [`{{short_sha}}`]({{full_commit_url}}) | `{{base_ref}}` | `{{profile}}` | `{{utc_iso8601}}` |

{{one_or_two_sentence_conclusion}}

### Quality matrix

| Dimension | State | Summary |
| --- | --- | --- |
| Correctness and regressions | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Security and privacy | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Test comprehensiveness | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Architecture and compatibility | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Code quality and conventions | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Documentation and operational clarity | {{dimension_state}} | {{concise_evidence_based_summary}} |
| UI, UX, and accessibility | {{dimension_state}} | {{concise_evidence_based_summary}} |
| Performance and reliability | {{dimension_state}} | {{concise_evidence_based_summary}} |

### Findings

#### Blockers

{{blocker_entries_or_none}}

#### Warnings

{{warning_entries_or_none}}

#### Improvements

{{improvement_entries_or_none}}

### Deterministic checks

| Check | Result | Evidence |
| --- | --- | --- |
| {{exact_command_or_check_name}} | {{check_result}} | {{concise_observed_result}} |

### Review notes

- **Policy sources:** {{effective_global_repository_project_and_task_sources}}
- **Historical context:** {{material_history_and_effect_or_none}}
- **Adjudication:** {{adjudication_state}} — {{concise_result_or_reason}}
- **Rejected findings:** {{ids_and_short_reasons_or_none}}
- **Follow-ups:** {{ids_and_short_reasons_or_none}}

### Limitations and next action

- **Limitations:** {{limitations_or_none}}
- **Next action:** {{single_smallest_next_action_or_none}}

<details>
<summary>Reviewer receipt</summary>

| Role | Runner | Provider | Model | Capability | Effort | Fallback |
| --- | --- | --- | --- | --- | --- | --- |
| {{role}} | {{runner}} | {{provider}} | {{model}} | {{capability_tier}} | {{normalized_effort}} / {{native_effort}} | {{fallback_or_none}} |

</details>

> This reports source-code review evidence only; it is not proof of end-to-end product behavior.
````

Finding entries use this exact shape and retain the same finding ID across reruns when the underlying defect is unchanged:

```markdown
- **{{finding_id}} — {{title}}** (`{{confidence_percent}}%`) — {{impact}} [Evidence]({{immutable_full_sha_line_url}})
  - Smallest fix: {{remediation}}
```

If no deterministic check is applicable or runnable, retain the table and use one row with the check name, `NOT_RUN` or `BLOCKED`, and the exact reason. Never imply that a check passed when it did not run.

Every accepted blocker or warning must include an immutable GitHub permalink using the full reviewed SHA and an exact line range with useful surrounding context. Do not link to a moving branch ref.

## Freshness gate

Immediately before writing, re-fetch the pull request and compare its repository, number, open state, full head SHA, head ref, and base ref with the frozen target. Do not publish if any value changed. Report publication as `stale`, preserve the reviewed and current values, and require a new run against the new head.

State prominently that a clean source review is not proof of end-to-end product behavior.

## Inline comments and merge state

- The canonical summary comment is required when publication is authorized.
- Add inline comments only for accepted blockers or material warnings with an exact changed-line location, when the user or project policy explicitly requests inline publication.
- Deduplicate inline comments across reruns.
- Do not submit approval, request-changes, merge, label, assign, or change checks/statuses unless separately requested.

## Publication result

Report one of:

- `published`: canonical comment created or updated for the reviewed SHA.
- `skipped_by_user`: publication disabled by the user.
- `stale`: the pull request changed or closed after the review target was frozen.
- `owed`: a matching pull request exists but publication failed or lacked authorization.

Publication failure never changes the source-review result. Preserve the complete report in the session and include the failure reason.
