# Project Review Overrides

The canonical optional project manifest is `docs/code-review/review-policy.yml` or `.yaml`. A project contains at most one. Absence is normal and leaves the portable gate defaults in force.

## Compatible dimensions

The shared policy keys are:

- `correctness`
- `security`
- `testing`
- `architecture`
- `code_quality`
- `documentation`
- `ui_accessibility`
- `performance_reliability`

The focused gate maps `correctness` to logical correctness, `security` to security, `testing` to test coverage, `architecture` and `code_quality` to architecture and style, and `documentation` to documentation. Apply configured UI/accessibility and performance/reliability rules to the closest focused gate dimension according to their concrete impact; one project source may inform more than one gate dimension when necessary. Preserve the original policy key in the cited basis.

## Manifest shape

```yaml
version: 1

reviews:
  architecture:
    source: docs/code-review/architecture.md

  code_quality:
    source: docs/code-review/code-quality.md
    mode: extend

  documentation:
    source: docs/code-review/documentation.md
```

Each review entry requires `source`. `mode` is optional and defaults to `extend`. `replace` is supported only when explicit, and replaces the portable subject-matter rubric for that policy key—not the gate's factual correctness floor, five output dimensions, evidence standard, or universal safety checks.

## Resolution and safety

- No local entry means use the portable baseline for that dimension.
- Narrower explicit project rules take precedence when extending the baseline.
- Task-specific instructions apply after project resolution.
- Project rules cannot make a demonstrated runtime failure, security vulnerability, authorization bypass, data-loss risk, or explicit acceptance-criterion violation disappear.
- Resolve `source` relative to the repository root. Reject absolute paths, `..` traversal, missing files, repository-escaping symlinks, remote content, unknown dimensions, unknown modes, unsupported versions, and duplicate YAML keys when detectable.
- If both manifest spellings exist, treat the configured project policy as ambiguous and block the affected project-conformance decisions.
- When a source is invalid, still perform the safe portable baseline and label the affected result baseline-only rather than silently claiming project-policy conformance.

Record every effective global, repository-instruction, project-policy, and task-specific source in `policy_sources`.
