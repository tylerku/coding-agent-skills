# Project Review Overrides

The canonical optional project manifest is `docs/code-review/review-policy.yml` or `.yaml`. A project should contain at most one.

## Supported dimensions

- `correctness`
- `security`
- `testing`
- `architecture`
- `code_quality`
- `documentation`
- `ui_accessibility`
- `performance_reliability`

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

  testing:
    source: docs/code-review/testing.md
    mode: replace
```

Each review entry requires `source`. `mode` is optional and defaults to `extend`.

## Resolution

- No local entry: use the global dimension rubric.
- `mode: extend`: concatenate the global principles with the project rubric, then resolve narrower explicit project rules in favor of the project.
- `mode: replace`: use the project subject-matter rubric instead of the global dimension rubric.
- Task-specific instructions apply after project resolution.
- The specialist output contract, independence requirement, consolidated finding adjudication, factual correctness floor, and concrete safety checks are never replaced.

Project rules may replace architecture, naming, logging, testing, or style preferences. They cannot make a demonstrated runtime failure, security vulnerability, authorization bypass, data-loss risk, or explicit acceptance-criterion violation disappear.

## File safety and validity

- Resolve `source` relative to the repository root.
- Reject absolute paths, `..` traversal, missing files, and symlinks that escape the repository.
- Reject unknown dimensions, unknown modes, unsupported versions, and duplicate YAML keys when the parser exposes them.
- Do not fetch remote rubric content from the manifest.
- When both manifest spellings exist and both are readable, mark the union of their locally configured dimensions `blocked` for project-policy conformance. Continue dimensions absent from both with their global rubrics.
- When a manifest is malformed or cannot be safely resolved, mark project-policy conformance `blocked` for every dimension whose effective local rules cannot be determined. Still perform the global baseline audit and label its findings as baseline-only rather than silently treating the global rubric as the effective project policy.
- Never stop correctness, security, or other safe baseline inspection merely because one project override is invalid.

Record the effective sources and mode in the final matrix.

## Reviewer mappings

A project may provide `docs/code-review/reviewers.yml` to extend or override concrete provider mappings. Use the schema concepts in the skill's `reviewer-models.yml`.

- Project provider entries extend shipped providers by default.
- A project may replace one provider entry with `mode: replace` when its parser or wrapper supports that envelope.
- Explicit user choices and cost ceilings still take precedence.
- Reject unknown capability tiers, reasoning efforts, unsafe file references, and unmapped runner/provider combinations.
- Never infer that an unlisted model satisfies a capability tier. Add the mapping or mark the role `owed`.
- Record both the mapping source and actual resolved reviewer in the final report.
