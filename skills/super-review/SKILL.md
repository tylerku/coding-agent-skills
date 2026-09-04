---
name: super-review
description: Resolve or safely create a draft GitHub pull request, run a comprehensive provider-neutral code review, repair clear accepted findings when authorized, verify the resulting head, and publish standard review state. Use for an explicitly requested super review, exhaustive PR review, or comprehensive quality audit. Do not use for an ordinary narrow review or as a substitute for product smoke testing.
---

# Comprehensive Code Review and Remediation

Audit a frozen GitHub pull request through parallel specialist reviewers, deterministic code evidence, historical context, consolidated finding adjudication, bounded remediation of clear findings, and a final completeness matrix. Keep reviewer roles independent of AI provider and never present source review as proof that a running product works.

## Operating Contract

- An explicitly requested super review authorizes one bounded repair wave on the matching pull-request branch for accepted blockers and warnings whose smallest correct fix is clear and decision-free, unless the user requests report-only behavior. Use an isolated checkout when practical, preserve unrelated work, and ask immediately before mutation when the host or repository requires separate confirmation.
- An explicit super-review request authorizes one normal push of already committed feature-branch state and one draft pull-request creation when no matching PR exists and every condition in [references/pr-target.md](references/pr-target.md) is satisfied. It never authorizes committing dirty work or choosing among ambiguous repositories, branches, or bases. If invocation was implicit or the host requires separate confirmation, ask immediately before either write.
- Do not create a branch or non-draft pull request, force-push, rebase, merge, deploy, submit an approving or changes-requested review, repair unrelated debt, or mutate production data or external systems.
- Exactly one matching open GitHub pull request is mandatory before specialist dispatch. It may be pre-existing or safely bootstrapped as a draft. Draft pull requests are eligible unless the user or project policy excludes them. If a unique target cannot be resolved or safely created, stop before dispatch and report `blocked`.
- An explicitly requested super-review includes permission to update one canonical informational comment on a matching existing pull request unless the user opts out. If the skill was activated without a clear request or the host requires separate approval, obtain authorization immediately before posting.
- Freeze the target before dispatch: base GitHub repository, pull-request number and URL, authoritative head repository owner/name, full head SHA, head ref, base ref, task intent, acceptance criteria, changed files, affected systems, out-of-scope boundaries, and non-test LOC when practical.
- Review the current change, not the entire backlog. Record important adjacent problems as follow-ups only when evidence makes them material.
- Treat severity and confidence as separate fields. A severe hypothesis with weak evidence is not a confirmed blocker.
- A builder self-check is supplemental. It never satisfies an independent specialist lane.
- Do not claim perfection. A clean result means every applicable source-review dimension was examined with sufficient code evidence and no unresolved findings remain. It does not prove end-to-end behavior.
- Do not depend on a smoke-test or acceptance-verification skill. Consume supplied runtime evidence when useful, but complete the source review without it.
- A fixed finding is not complete until the repair is committed, pushed to the PR head, and verified against the resulting full SHA. Never describe a suggestion, local edit, or unverified attempt as fixed.

## Host Compatibility

Use the host's native skill, delegation, shell, filesystem, image, and GitHub mechanisms. When running in Claude Code, read [references/claude-code.md](references/claude-code.md) before dispatching specialists. `agents/openai.yaml` is optional Codex interface metadata and is not part of the review contract.

## 1. Resolve or Create and Freeze the GitHub Pull Request

Establish the expected base ref before PR discovery using this precedence: explicit user direction, applicable repository instructions, existing authoritative branch metadata, then an unambiguous repository default. If sources conflict or none establishes a safe base, report `blocked`; do not use an existing PR to silently choose the contract.

Then resolve exactly one open GitHub pull request from an explicit URL or number, or from the current repository and authoritative head ref. Never select by title similarity alone. If the user named a PR URL or number that is missing, closed, or otherwise ineligible, report `blocked`; do not substitute a newly created PR. Require every existing candidate's base to match the established expected base. A different-base PR is a target conflict: report it and stop rather than reviewing the wrong diff or creating a second PR automatically. When the request targets the current change without naming an unresolved PR and no open PR exists for that head, read [references/pr-target.md](references/pr-target.md) and bootstrap one draft PR only when its full safety contract passes.

After resolving or creating the PR, confirm the base repository identity, authoritative head repository owner/name, head ref, and full head SHA before collecting evidence or launching reviewers. Treat a fork head as a distinct push target even when its branch name also exists in the base repository. If more than one match remains, target identity is uncertain, safe bootstrap is unavailable, or the authoritative diff cannot be read, report `blocked` and stop. Do not install or authenticate GitHub tooling without authorization.

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
| Documentation and operational clarity | [references/documentation.md](references/documentation.md) |
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

Launch one `historical_context` specialist in parallel with the applicable dimension specialists. Read [references/historical-context.md](references/historical-context.md). Its evidence and candidate findings feed the relevant dimensions; it is not a ninth matrix dimension.

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

## 8. Repair Clear Accepted Findings

Read [references/remediation.md](references/remediation.md). Classify every accepted blocker and warning as `auto_fix`, `decision_required`, or `repair_owed`. Improvements are report-only unless the user explicitly requests them.

Repair all `auto_fix` findings in one coordinated implementation wave. Do not let parallel agents edit the same worktree. Before pushing, run the authoritative focused checks, confirm the original PR head repository, ref, and SHA are unchanged, and use a normal non-force push to that exact head repository and ref. If any target identity or SHA changed, stop and report `stale`; never overwrite another contributor's update.

After a successful push, freeze the resulting head SHA. Re-run deterministic checks and independent specialist review for every dimension that had an accepted finding or is materially affected by the repair diff. Carry an earlier passing lane forward only when its reviewed scope is unchanged, and record that basis. If a repair introduces or exposes another accepted finding, leave it open after this one bounded repair wave rather than looping.

Set each accepted finding to `fixed`, `open`, `decision_required`, or `repair_owed`. Preserve its original finding ID and first-seen SHA. A repair is `fixed` only when verification passes on the pushed final SHA.

## 9. Synthesize

The primary orchestrator verifies accepted findings against the repository, deduplicates them by underlying defect, resolves cross-dimension conflicts, and reports:

1. Review target and contract.
2. Deterministic commands and observed results.
3. Dimension matrix: `pass`, `pass_after_fixes`, `findings`, `decision_required`, `not_applicable`, `owed`, or `blocked`.
4. Accepted findings grouped by resolution state, including first-seen and fixed SHAs.
5. Rejected and follow-up findings with short reasons.
6. Historical evidence and whether it changed any conclusion.
7. Provider, model, runner, capability tier, reasoning effort, and fallback used per role.
8. Rubric sources used per dimension.
9. Runtime limitations and other remaining uncertainty.
10. Initial and final reviewed SHAs, repair commit and checks, pull-request publication state, and the smallest next action.

Compute each final matrix status after repair verification. Use this precedence: `blocked`, then `owed`, then `decision_required`, then `findings`, then `pass_after_fixes`, then `pass`; `not_applicable` is used only when the lane truly does not apply. A `blocked` or `owed` lane may still list accepted findings. Use `pass_after_fixes` only when every accepted finding in that lane was verified fixed on the final SHA. If every proposed finding is rejected and evidence is otherwise sufficient, the final lane becomes `pass`.

Do not report the audit as clean when any applicable source-review dimension is `owed` or `blocked`, or when any accepted finding remains unresolved. Do not launch redundant reviewers merely to obtain nicer wording.

## 10. Publish Existing Pull-Request State

Read [references/pr-reporting.md](references/pr-reporting.md). Always present the complete report in the session.

Immediately before publication, re-fetch the pull request and verify that it remains open and its base repository, number, authoritative head repository, full final head SHA, head ref, and base ref still match the frozen final target. If any value changed, do not publish the stale result; report `stale` with the reviewed and current values and require a new run.

When freshness is confirmed and publication is authorized, render the exact canonical structure in [references/pr-reporting.md](references/pr-reporting.md) and create or update exactly one informational comment identified by `<!-- super-review-report:v4 -->`. Preserve its heading order, status vocabulary, empty states, finding history, repair receipt, and reviewer-receipt table on every run. If publishing fails, preserve the complete session report and mark publication `owed`; do not change the source-review result.
