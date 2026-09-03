---
name: pr-review
description: Run a focused, provider-neutral, single-reviewer must-fix gate on an open GitHub pull request. Use when PR automation or a user needs a fast merge-safety decision covering architecture and style, test coverage, applicable documentation, security, and logical correctness. Do not use as a comprehensive replacement for super-review.
---

# PR Must-Fix Gate

Decide whether the exact pull-request SHA contains any concrete issue that must be fixed before merge. Optimize for high-confidence merge safety, low noise, and fast automatic execution rather than comprehensive quality coverage.

## Operating contract

- Review one open GitHub pull request and bind the result to its full head SHA and base SHA.
- Use exactly one cold independent reviewer. Do not spawn subagents, invoke another review skill, edit code, commit, push, approve, request changes, close, or merge.
- The surrounding automation owns event triggering and required-check enforcement. Publish a GitHub check or canonical comment only when the invocation explicitly grants that write.
- Use a minimum `advanced` capability reviewer with `high` reasoning effort. Use `frontier` capability for authentication, authorization, payments, secrets, sensitive data, irreversible writes, material data-loss risk, concurrency, distributed state, or subtle financial/time invariants. Resolve the concrete provider model through [references/reviewer-models.yml](references/reviewer-models.yml). If the required capability is unavailable, return `BLOCKED` rather than silently downgrading.
- Report only problems introduced or exposed by the PR. Record material legacy debt as a warning only when it directly affects the changed path.
- A clean gate means no must-fix issue was found in the five focused dimensions. It is not a comprehensive audit or proof of end-to-end behavior.

## Host compatibility

Use the host's native skill, shell, filesystem, and GitHub mechanisms. When running in Claude Code, read [references/claude-code.md](references/claude-code.md) before reviewing. `agents/openai.yaml` is optional Codex interface metadata and is not part of the gate contract.

## 1. Freeze the pull request

Resolve exactly one open GitHub pull request from an explicit URL or number, or from the current repository and head ref. Record repository, PR number and URL, full head SHA, full base SHA, head ref, base ref, and changed files. Never select by title similarity.

If the PR or authoritative diff cannot be resolved unambiguously, return `BLOCKED` and stop. Do not fall back to uncommitted changes, a branch-only diff, or an inferred directory scope.

## 2. Resolve the review contract

Read the PR description, linked task or issue when available, applicable `AGENTS.md` and `CLAUDE.md` files, and relevant project documentation. Explicit requirements and repository rules are authoritative; tests and existing behavior are compatibility evidence, not automatic product authority.

Do not invent missing product decisions. A missing decision is `BLOCKED` only when it prevents a responsible merge-safety judgment; otherwise record the limitation and continue.

## 3. Resolve project review policy

The portable five-dimension rubric is the fallback baseline. Look for exactly one optional project manifest:

- `docs/code-review/review-policy.yml`
- `docs/code-review/review-policy.yaml`

When one exists, read [references/project-overrides.md](references/project-overrides.md), load every safely referenced rubric, and extend the baseline by default. Record each effective source and mode in the gate result. A malformed or ambiguous project policy blocks only the affected project-conformance decision; continue every safe baseline check and label it baseline-only.

## 4. Collect focused evidence

Inspect the complete PR diff plus the minimum adjacent code needed to trace changed behavior. Consume current CI results when available. Run focused non-destructive tests, typechecks, static checks, or searches only when they materially resolve a gate decision; do not duplicate an already authoritative passing CI check without reason.

If evidence needed to exclude a critical failure cannot be collected, return `BLOCKED`. Missing optional evidence is a limitation, not automatically a gate failure.

## 5. Review the five dimensions

Read [references/review-dimensions.md](references/review-dimensions.md). Evaluate, in this order:

1. Logical correctness.
2. Security.
3. Architecture and style.
4. Test coverage.
5. Documentation applicability and adequacy.

Every dimension appears in the report as `pass`, `findings`, `not_applicable`, or `blocked`. Documentation may be `not_applicable` with a concrete reason; the other dimensions normally apply to every code change.

## 6. Apply the must-fix bar

Classify a finding as `must_fix` only when both are true:

- The defect or explicit-rule violation is supported with confidence of at least `0.80` by traced code, deterministic evidence, or an unambiguous project requirement.
- Merging without correction creates a concrete correctness, security, compatibility, operability, maintainability, or required-proof failure.

Use `warning` for real but non-blocking risk. Do not report optional polish, speculative optimization, or preference-only advice. If a potentially critical concern cannot be confirmed or dismissed, return `BLOCKED` with the missing evidence instead of manufacturing a must-fix finding.

Deduplicate symptoms into one root-cause finding and give the smallest appropriate fix. Require exact changed-line or directly affected-contract citations.

## 7. Decide, refresh, and report

Use [references/output-contract.md](references/output-contract.md). Compute the gate:

- `FAIL`: one or more accepted `must_fix` findings.
- `BLOCKED`: a responsible gate decision cannot be completed.
- `PASS`: no must-fix findings remain; warnings may still exist.
- `STALE`: the PR head or base changed after the target was frozen.

Immediately before returning or publishing, re-fetch the PR and compare repository, number, open state, full head SHA, and full base SHA. A stale result must not update the current gate. When GitHub publication is authorized, follow [references/automation-contract.md](references/automation-contract.md).
