# Canonical Smoke-Test Report Contract

Build one normalized report after the pass, then render it in every destination. The session and pull-request versions use the exact structure, identifiers, status vocabulary, ordering, content, and empty states below. Never generate a shorter independent PR summary that can drift from the session result.

## Normalized report rules

- Overall status: `PASS`, `FAIL`, `BLOCKED`, or `STALE`.
- Case status: `PASS`, `FAIL`, `BLOCKED`, or `NOT_APPLICABLE`.
- Session delivery status: `DELIVERED` or `OWED`. Use `DELIVERED` only when the complete report and every required screenshot or accessible artifact are present in the requesting session.
- Pull-request publication status: `CREATED`, `UPDATED`, `NOT_APPLICABLE`, `OWED`, or `WITHHELD_STALE`.
- Journey IDs: `J01`, `J02`, and so on, ordered by execution.
- Challenge IDs: `C01`, `C02`, and so on, ordered by execution.
- Checkpoint IDs: `<case-id>-<viewport>-<two-digit-order>`, such as `J01-desktop-02` or `C03-na-01`.
- Defect IDs: `D01`, `D02`, and so on, ordered by first observation.
- Surface categories use the canonical IDs in `risk-scaled-testing.md`.
- Use `None.` for every empty prose section and `None` for an empty table cell.
- Preserve the same case, checkpoint, defect, and screenshot order in every destination.
- Render all timestamps as UTC ISO-8601 and commits as immutable full-SHA links when a repository URL exists.

## Destination adaptation

The report body is identical in the session and pull request.

- Session: omit the HTML marker. Display every screenshot inline or as an image attachment when supported, and include its absolute local path or authorized URL. A path alone is insufficient when the host can render the image. After PR publication, include the resulting comment URL.
- Pull request: prepend `<!-- smoke-test-report:v3 -->`. Replace local-only paths with confirmed reviewer-accessible artifact URLs and embed every image inline. Do not omit a checkpoint because its image could not be uploaded; retain the checkpoint, state the evidence debt, and set publication to `OWED`. In its own publication row, use `This canonical comment` instead of requiring a self-referential URL.
- Redact a base URL, artifact path, or observation only when exposure would be unsafe. Use the same redacted value in both renderings.

## Exact template

```markdown
{{optional_pr_marker}}
## Smoke Test

| Result | Tested commit | Depth | Environment | Tested at |
| --- | --- | --- | --- | --- |
| **{{overall_status}}** | {{commit_link_or_sha}} | {{focused_standard_or_deep}} | {{environment}} | `{{utc_iso8601}}` |

### Test receipt

| Field | Value |
| --- | --- |
| Repository | {{owner_name_or_local_path}} |
| Branch | {{tested_branch_or_detached_head}} |
| Worktree | {{clean_or_dirty_with_changed_file_inventory}} |
| Pull request | {{url_or_none}} |
| Base URL | {{url_redacted_when_necessary}} |
| Server provenance | {{process_receipt_or_matching_build_identity}} |
| Harness | {{playwright_project_runner_api_client_or_other}} |
| Browser | {{browser_names_and_versions_or_not_applicable}} |
| Actors | {{tested_roles_or_system_actors}} |
| Test data | {{synthetic_fixture_seed_or_authorized_profile_without_credentials}} |
| Flags and configuration | {{relevant_nonsecret_profiles_or_none}} |
| Artifacts | {{storage_location_and_access_classification}} |
| Test depth rationale | {{why_this_depth_applies}} |
| Policy sources | {{explicit_request_and_project_files_or_none}} |

### Feature surface

| Category | Applicability | Affected surface | Challenge coverage |
| --- | --- | --- | --- |
| `{{canonical_category_id}}` | {{applicable_or_not_applicable}} | {{affected_surface_or_reason}} | {{case_ids_or_not_required_at_depth}} |

### Journey and challenge summary

| ID | Case | Type | Surface | Hypothesis or selection reason | Evidence | State |
| --- | --- | --- | --- | --- | --- | --- |
| {{case_id}} | {{case_name}} | {{journey_or_challenge}} | {{category_ids}} | {{reason_or_defect_hypothesis}} | {{ui_api_database_provider_log_or_other}} | **{{case_status}}** |

### Checkpoint evidence

#### {{case_id}} · {{case_name}} · {{viewport_or_nonvisual}}

1. **{{checkpoint_id}} · {{checkpoint_name}} — {{checkpoint_status}}**
   - Action: {{action_or_condition_established}}
   - Expected: {{expected_observable_state}}
   - Observed: {{actual_observed_state}}
   - Runtime: {{relevant_console_network_persistence_provider_or_recovery_evidence_or_none}}
   - Artifact: {{absolute_local_path_or_authorized_url_or_none}}

   {{inline_screenshot_or_not_applicable}}

### Defects found

#### {{stable_defect_id}} · {{short_title}}

- Case: {{case_and_checkpoint_ids}}
- Reproduction: {{concise_observed_reproduction}}
- Impact: {{user_or_system_consequence}}
- Evidence: {{artifact_and_runtime_evidence}}

{{defect_entries_or_none}}

### Runtime observations

{{relevant_console_network_persistence_provider_retry_and_baseline_observations_or_none}}

### Limitations and next action

{{untested_surfaces_evidence_debt_environment_constraints_and_smallest_next_action_or_none}}

### Publication

| Destination | State | Detail |
| --- | --- | --- |
| Session | {{session_delivery_status}} | {{inline_image_attachment_or_accessible_artifact_detail}} |
| Pull request | {{pull_request_publication_status}} | {{comment_reference_url_or_reason}} |

> This is a risk-scaled runtime challenge of the affected feature, not a source-code review or unrelated whole-product regression suite.
```

Repeat surface, case, checkpoint, and defect rows or blocks as needed without changing the heading order. When there are no defects, replace the entire defect-entry body with `None.` and retain the heading.

## Completeness

Before rendering either destination, confirm:

- every mapped surface category has exactly one row;
- every selected journey and challenge has a stable ID and summary row;
- every executed checkpoint appears once in execution order;
- every visual checkpoint has the same screenshot in both destinations, adapted only by location;
- every failed checkpoint maps to a defect or an explicit blocked limitation;
- the overall result, session delivery state, and pull-request publication state follow their destination-specific vocabularies above;
- no destination contains a conclusion absent from the normalized report.
