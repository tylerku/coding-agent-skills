---
name: super-review
description: Run a comprehensive, evidence-backed, provider-neutral review of an open GitHub pull request across every applicable source-code quality dimension, then publish a standard review-state comment. Use for an explicitly requested super review, exhaustive PR review, or comprehensive quality audit. Do not use without a matching GitHub PR, for an ordinary narrow review, or as a substitute for product smoke testing.
---

# Comprehensive Code Review

Audit a frozen GitHub pull request through parallel specialist reviewers, deterministic code evidence, historical context, consolidated finding adjudication, and a final completeness matrix. Keep reviewer roles independent of AI provider and never present source review as proof that a running product works.

## Operating Contract

- Review source and report results only. Do not edit code, commit, push, create a pull request, submit an approving or changes-requested review, or mutate unrelated state.
- A matching open GitHub pull request is mandatory. Draft pull requests are eligible unless the user or project policy excludes them. If exactly one matching pull request cannot be resolved, stop before dispatch and report `blocked`; never create a pull request to satisfy this requirement.
- An explicitly requested super-review includes permission to update one canonical informational comment on a matching existing pull request unless the user opts out. If the skill was activated without a clear request or the host requires separate approval, obtain authorization immediately before posting.
- Freeze the target before dispatch: GitHub repository, pull-request number and URL, full head SHA, head ref, base ref, task intent, acceptance criteria, changed files, affected systems, out-of-scope boundaries, and non-test LOC when practical.
- Review the current change, not the entire backlog. Record important adjacent problems as follow-ups only when evidence makes them material.
- Treat severity and confidence as separate fields. A severe hypothesis with weak evidence is not a confirmed blocker.
- A builder self-check is supplemental. It never satisfies an independent specialist lane.
- Do not claim perfection. A clean result means every applicable source-review dimension was examined with sufficient code evidence and no unresolved findings remain. It does not prove end-to-end behavior.
- Do not depend on a smoke-test or acceptance-verification skill. Consume supplied runtime evidence when useful, but complete the source review without it.

## 1. Require and Freeze the GitHub Pull Request

Resolve exactly one open GitHub pull request from an explicit URL or number, or from the current repository, head ref, and expected base. Never select by title similarity alone. Confirm the remote repository identity and record the full head SHA before collecting evidence or launching reviewers.

If no matching open pull request exists, more than one match remains, the repository identity is uncertain, or the pull-request diff cannot be read, report `blocked` and stop. Do not install or authenticate GitHub tooling without authorization.

## 2. Build the Review Contract

Derive intended behavior in this precedence order:

1. Explicit user instructions in the current request.
2. A pinned task, issue, PR, or tracker specification supplied or discoverable in scope.
3. Applicable repository instructions such as `AGENTS.md` and `CLAUDE.md`.
4. Project specifications and architecture documentation.
5. Existing tests and observable behavior as supporting evidence, not automatic product authority.
6. Clearly labeled inference.

Read [references/review-contract.md](references/review-contract.md) when acceptance criteria are missing, distributed, conflicting, or inferred.

Do not silently invent product decisions. If behavioral acceptance criteria remain materially incomplete, continue the code-quality audit but mark behavioral conformance `owed` or `blocked`.

## 3. Resolve Effective Review Rubrics

The global dimension references are the fallback baseline. Before dispatch, look for:

- `docs/code-review/review-policy.yml`
- `docs/code-review/review-policy.yaml`

If either exists, read [references/project-overrides.md](references/project-overrides.md) and resolve each dimension independently. Project definitions extend the global rubric by default. `mode: replace` must be explicit. An invalid or ambiguous local policy blocks only the affected project-conformance decision; continue every safe baseline review that can still be performed and label the limitation.

Also apply relevant `AGENTS.md`, `CLAUDE.md`, linked architecture/style documents, and task-specific constraints. Record every rubric source given to a specialist.

## 4. Determine Applicable Dimensions

Always assess applicability for:

| Dimension | Global rubric |
| --- | --- |
| Correctness and regressions | [references/correctness.md](references/correctness.md) |
| Security and privacy | [references/security.md](references/security.md) |
| Test comprehensiveness | [references/testing.md](references/testing.md) |
| Architecture and compatibility | [references/architecture.md](references/architecture.md) |
| Code quality and conventions | [references/code-quality.md](references/code-quality.md) |
| UI, UX, and accessibility | [references/ui-accessibility.md](references/ui-accessibility.md) |
| Performance and reliability | [references/performance-reliability.md](references/performance-reliability.md) |

An inapplicable dimension still appears in the final matrix with a concrete reason. Do not launch a specialist merely to return an obvious `not_applicable` result.

## 5. Collect Deterministic Code Evidence

Discover authoritative repository commands from instructions, package scripts, CI, and existing tooling. Run applicable non-destructive checks in proportion to the change:

- typecheck, compile, build, lint, static analysis;
- focused tests, broader tests, and coverage when it answers a real coverage question;
- secret and dependency scanning when configured;
- prohibited-pattern checks defined by the project;
- migrations/schema validation when authorized and feasible;
- benchmarks, bundle measurements, query plans, or request/render counts for material performance claims.

Do not run a comprehensive product journey or create proof screenshots as part of this skill. Existing screenshots, acceptance reports, API observations, and other runtime artifacts may inform the review, but their absence does not block a source-code conclusion. Record runtime limitations in `unknowns`. If an authoritative source-code check cannot run, preserve the error and mark the affected evidence `owed` or `blocked`.

## 6. Resolve Reviewers and Dispatch Independent Specialists

Read [references/model-routing.md](references/model-routing.md), [references/reviewer-requirements.yml](references/reviewer-requirements.yml), and [references/reviewer-models.yml](references/reviewer-models.yml) before dispatch. Preserve any explicit user provider, model, profile, or cost ceiling. Otherwise use the Balanced profile.

Roles specify `capability_tier` and normalized `reasoning_effort`; provider adapters map those requirements to concrete models and native effort values. Apply this precedence:

1. Explicit user choices and ceilings.
2. Project `docs/code-review/reviewers.yml` definitions.
3. Shipped reviewer mappings.
4. A disclosed same-or-higher-capability fallback.

Never invent a model-to-tier classification during a run, silently downgrade capability, or cross a cost ceiling. When no eligible reviewer exists, mark the lane `owed`.

For every applicable dimension:

1. Launch an independent, report-only specialist through the host's supported delegation mechanism. Prefer a cold context that does not inherit the builder's rationale.
2. Provide only the frozen review contract, exact review target, relevant changed and adjacent files, effective dimension rubric, project instructions, and collected evidence.
3. Tell the specialist not to modify files, invoke nested reviewers, or expand scope.
4. Require the structure in [references/output-contract.md](references/output-contract.md).
5. Run independent specialists concurrently when slots permit; use waves rather than weakening coverage when they do not.

The code-quality lane has one `advanced` judgment owner. Feed it a `routine` mechanical prepass for naming, comments, logger usage, explicit convention matching, and citation checks. The prepass supplies evidence and candidate findings; it does not replace the independent code-quality specialist or decide material maintainability issues. Treat invariant, ordering, compatibility, workaround, and safety comments as local contracts unless stronger current requirements supersede them.

Launch one `historical_context` specialist in parallel with the applicable dimension specialists. Read [references/historical-context.md](references/historical-context.md). Its evidence and candidate findings feed the relevant dimensions; it is not an eighth matrix dimension.

Do not count the primary orchestrator or an implementation agent as an independent specialist.

## 7. Adjudicate Material Findings Once

After the parallel specialists finish, collect all proposed `blocker` and material `warning` findings into one deduplicated packet. If the packet is non-empty, launch one independent `finding_adjudication` reviewer. Use the critical adjudication role for high-risk findings or conflicting specialist conclusions. Do not launch one validator per finding and do not run a separate cold backstop panel.

The adjudicator must attempt to disprove each finding by checking:

- whether it is introduced or exposed by the reviewed change;
- the actual code path and unchanged adjacent context;
- project and dependency contracts;
- reachability and realistic triggering conditions;
- existing tests or deterministic evidence;
- the cited project or universal rule;
- whether the proposed fix belongs inside scope.

Classify each finding as `accepted`, `rejected`, `follow_up`, or `escalated`. Preserve a brief reason and the adjudicator's updated confidence. The primary orchestrator may verify citations and resolve duplicates, but it must not silently overturn a material adjudication; disclose any unresolved disagreement.

## 8. Synthesize

The primary orchestrator verifies accepted findings against the repository, deduplicates them by underlying defect, resolves cross-dimension conflicts, and reports:

1. Review target and contract.
2. Deterministic commands and observed results.
3. Dimension matrix: `pass`, `findings`, `not_applicable`, `owed`, or `blocked`.
4. Accepted blockers, warnings, and improvements.
5. Rejected and follow-up findings with short reasons.
6. Historical evidence and whether it changed any conclusion.
7. Provider, model, runner, capability tier, reasoning effort, and fallback used per role.
8. Rubric sources used per dimension.
9. Runtime limitations and other remaining uncertainty.
10. Pull-request publication state and the smallest next action.

Compute each final matrix status after finding adjudication. Use this precedence: `blocked`, then `owed`, then `findings`, then `pass`; `not_applicable` is used only when the lane truly does not apply. A `blocked` or `owed` lane may still list accepted findings. If every proposed finding is rejected and evidence is otherwise sufficient, the final lane becomes `pass`.

Do not report the audit as clean when any applicable source-review dimension is `owed` or `blocked`, or when any accepted finding remains unresolved. Do not launch redundant reviewers merely to obtain nicer wording.

## 9. Publish Existing Pull-Request State

Read [references/pr-reporting.md](references/pr-reporting.md). Always present the complete report in the session.

Immediately before publication, re-fetch the pull request and verify that it remains open and its repository, number, full head SHA, head ref, and base ref still match the frozen target. If any value changed, do not publish the stale result; report `stale` with the reviewed and current values and require a new run.

When freshness is confirmed and publication is authorized, render the exact canonical structure in [references/pr-reporting.md](references/pr-reporting.md) and create or update exactly one informational comment identified by `<!-- super-review-report:v2 -->`. Preserve its heading order, status vocabulary, empty states, finding format, and reviewer-receipt table on every run. If publishing fails, preserve the complete session report and mark publication `owed`; do not change the source-review result.
