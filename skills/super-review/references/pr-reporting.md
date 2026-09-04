# Pull-Request Reporting

Always return the complete review in the active session. Pull-request publication mirrors that result; it is not the only copy.

## Discovery and authorization

- Resolve exactly one matching open GitHub pull request from the frozen base repository, authoritative head repository owner/name, head ref or commit, and expected base. Never review or post to a title match or a merely similar branch.
- A matching GitHub pull request is a prerequisite for specialist dispatch, not merely an optional reporting destination. It may be pre-existing or safely created as a draft through `pr-target.md`. Draft pull requests remain eligible unless project policy says otherwise.
- Never create a branch or non-draft pull request. Before review, pushes and draft creation are allowed only through the target-bootstrap contract; after review, repairs may push only through the bounded remediation contract.
- An explicitly requested super-review authorizes eligible target bootstrap, the bounded repair wave, and updating the canonical informational comment unless the user opts out. If invocation was implicit, repository ownership is unclear, or the host requires confirmation, ask immediately before a write.
- Honor project instructions and code-host permissions. Do not install a CLI or authenticate a new account without authorization.

## Canonical comment

Use exactly one comment containing this marker as its first line:

```html
<!-- super-review-report:v4 -->
```

Search first for the v4 marker. For migration, also search for `<!-- super-review-report:v3 -->`, `<!-- super-review-report:v2 -->`, and `<!-- super-review-report:v1 -->`. Update an existing marked comment only when it is owned by the active reviewer identity; replace an owned older comment in place with the v4 structure and marker. Otherwise create one new v4 comment. Never edit another author's marked comment and never append a fresh comment on every rerun.

## Fixed rendering contract

Render the following structure exactly. Do not rename, reorder, or omit sections. Use `None.` for an empty finding or note group. Keep the conclusion to at most two sentences and keep table summaries to one concise sentence.

Allowed values:

- Overall state: `PASS`, `PASS_WITH_FIXES`, `FINDINGS`, `DECISION_REQUIRED`, `OWED`, `BLOCKED`.
- Dimension state: `PASS`, `PASS_AFTER_FIXES`, `FINDINGS`, `DECISION_REQUIRED`, `NOT_APPLICABLE`, `OWED`, `BLOCKED`.
- Finding resolution: `FIXED`, `OPEN`, `DECISION_REQUIRED`, `REPAIR_OWED`.
- Check result: `PASS`, `FAIL`, `NOT_RUN`, `BLOCKED`.
- Adjudication state: `COMPLETED`, `NOT_REQUIRED`, `OWED`.

Apply these formatting rules on every run:

- Compute overall state with this precedence: `BLOCKED`, then `OWED`, then `DECISION_REQUIRED`, then `FINDINGS`, then `PASS_WITH_FIXES`, then `PASS`. A `REPAIR_OWED` finding remains unresolved and therefore contributes `FINDINGS`.
- Use the first 12 characters of the initial and final SHAs, while every URL contains the full SHA. When no repair was pushed, both values are the same.
- Use a UTC timestamp formatted as `YYYY-MM-DDTHH:MM:SSZ`.
- Keep the eight dimension rows in the displayed order below.
- Group accepted findings by resolution state and sort by stable finding ID within each group.
- List deterministic checks in execution order and reviewer roles in workflow order.
- Escape pipe characters and collapse newlines inside table cells so Markdown tables remain valid.
- Do not add emojis, badges, extra headings, generated-by signatures, or prose outside the template.

````markdown
<!-- super-review-report:v4 -->
## Super Review

| State | Initial head | Final head | Base | Profile | Reviewed at |
| --- | --- | --- | --- | --- | --- |
| **{{overall_state}}** | [`{{initial_short_sha}}`]({{initial_full_commit_url}}) | [`{{final_short_sha}}`]({{final_full_commit_url}}) | `{{base_ref}}` | `{{profile}}` | `{{utc_iso8601}}` |

{{one_or_two_sentence_conclusion}}

### Remediation summary

| Accepted | Fixed | Open | Decision required | Repair owed | Repair commit |
| --- | --- | --- | --- | --- | --- |
| {{accepted_count}} | {{fixed_count}} | {{open_count}} | {{decision_count}} | {{repair_owed_count}} | {{repair_commit_link_or_not_applicable}} |

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

#### Fixed

{{fixed_entries_or_none}}

#### Open

{{open_entries_or_none}}

#### Decision required

{{decision_entries_or_none}}

#### Repair owed

{{repair_owed_entries_or_none}}

#### Improvements

{{improvement_entries_or_none}}

### Deterministic checks

| Check | Result | Evidence |
| --- | --- | --- |
| {{exact_command_or_check_name}} | {{check_result}} | {{concise_observed_result}} |

### Repair receipt

| Field | Value |
| --- | --- |
| Initial PR head | {{initial_full_sha}} |
| Repair workspace | {{isolated_worktree_or_clean_checkout_or_not_applicable}} |
| Push target | {{authoritative_head_repository_and_ref_or_not_applicable}} |
| Auto-fix disposition | {{ids_and_disposition_or_none}} |
| Repair commit and push | {{commit_push_result_or_not_applicable}} |
| Final PR head | {{final_full_sha}} |
| Post-repair review | {{rerun_dimensions_carried_lanes_and_result_or_not_applicable}} |

### Review notes

- **Policy sources:** {{effective_global_repository_project_and_task_sources}}
- **Historical context:** {{material_history_and_effect_or_none}}
- **Adjudication:** {{adjudication_state}} — {{concise_result_or_reason}}
- **Repair verification:** {{verification_summary_or_not_required}}
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

Fixed entries use this exact shape and retain the same finding ID across reruns when the underlying defect is unchanged:

```markdown
- **{{finding_id}} — {{title}}** (`{{severity}}`, `{{confidence_percent}}%`) — **FIXED** — {{impact}}
  - First seen: [evidence at `{{initial_short_sha}}`]({{immutable_initial_sha_line_url}})
  - Resolution: {{concise_repair_summary}}
  - Verified: [final code at `{{final_short_sha}}`]({{immutable_final_sha_line_url}}); {{verification_evidence}}
```

Open, decision-required, and repair-owed entries use this shape:

```markdown
- **{{finding_id}} — {{title}}** (`{{severity}}`, `{{confidence_percent}}%`) — **{{OPEN_OR_DECISION_REQUIRED_OR_REPAIR_OWED}}** — {{impact}}
  - Evidence: [first seen at `{{initial_short_sha}}`]({{immutable_initial_sha_line_url}})
  - {{Smallest_fix_or_decision_needed_or_owed_action}}: {{specific_next_step}}
```

If no deterministic check is applicable or runnable, retain the table and use one row with the check name, `NOT_RUN` or `BLOCKED`, and the exact reason. Never imply that a check passed when it did not run.

Every accepted blocker or warning must include immutable GitHub permalinks using the relevant full initial or final SHA and an exact line range with useful surrounding context. Do not link to a moving branch ref.

## Freshness gate

Immediately before writing, re-fetch the pull request and compare its base repository, number, open state, authoritative head repository owner/name, full head SHA, head ref, and base ref with the frozen final target. Do not publish if any value changed. Report publication as `stale`, preserve the reviewed and current values, and require a new run against the new head.

State prominently that a clean source review is not proof of end-to-end product behavior.

## Inline comments and merge state

- The canonical summary comment is required when publication is authorized.
- Add inline comments only for unresolved accepted blockers or material warnings with an exact changed-line location, when the user or project policy explicitly requests inline publication. Do not add a new inline comment for a finding already fixed by the same run.
- Deduplicate inline comments across reruns.
- Do not submit approval, request-changes, merge, label, assign, or change checks/statuses unless separately requested.

## Publication result

Report one of:

- `published`: canonical comment created or updated for the reviewed SHA.
- `skipped_by_user`: publication disabled by the user.
- `stale`: the pull request changed or closed after the review target was frozen.
- `owed`: a matching pull request exists but publication failed or lacked authorization.

Publication failure never changes the source-review result. Preserve the complete report in the session and include the failure reason.
