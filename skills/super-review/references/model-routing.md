# Reviewer Routing

Reviewer responsibility, model capability, and reasoning effort are separate decisions.

- A **role** defines the review responsibility.
- `capability_tier` defines the minimum configured model class: `routine`, `advanced`, or `frontier`.
- `reasoning_effort` defines normalized inference effort: `low`, `medium`, `high`, or `maximum`.
- `execution_mode` defines orchestration semantics such as `single_agent` or `multi_agent`; it never substitutes for reasoning effort.

The provider-neutral defaults are in [reviewer-requirements.yml](reviewer-requirements.yml). Concrete provider mappings are in [reviewer-models.yml](reviewer-models.yml).

## Resolution

Apply configuration in this order:

1. Explicit user provider, model, profile, or cost ceiling.
2. Repository `docs/code-review/reviewers.yml` entries.
3. Shipped provider mappings.
4. A disclosed same-or-higher-capability fallback allowed by the user's ceiling.

Select the role first, then its effective profile requirements, then a provider mapping. The orchestrator applies the map; it does not decide during a run that an unmapped model is `routine`, `advanced`, or `frontier`.

Never silently:

- downgrade `capability_tier`;
- reduce `reasoning_effort` when it is needed for a material judgment;
- replace an explicitly requested provider or model;
- cross a user cost ceiling;
- treat maximum effort on a routine model as frontier capability.

If no eligible configured reviewer is available, mark the role `owed`. Ask before crossing a ceiling. Record every actual runner, provider, model, native effort, and fallback in the final report.

The configured user preference disables Fable for Anthropic reviews and caps their effective reasoning effort at `high`. Apply `blocked_models` and `reasoning_effort_ceiling` from `reviewer-models.yml` after resolving role/profile requirements and before selecting the model or agent. This explicit user ceiling also applies to critical adjudication, the Maximum profile, project overrides, fallbacks, and host substitutions. Resolve frontier work to Opus 5 at high effort (or the configured Opus 4.8 alternative), never to Fable or native max effort. Do not treat earlier one-off Fable requests as overriding this saved preference; changing the preference requires a new explicit user instruction. Record the requested and effective efforts in the receipt.

## Profiles

Economy is the default. It keeps Balanced's role capability and reasoning requirements, including synthesis and adjudication, but groups related roles into fewer invocations as defined by `profiles.economy.reviewer_groups` in `reviewer-requirements.yml`. Balanced is an explicit opt-in and uses one independent invocation per applicable dimension plus historical context. Maximum retains separate specialists and applies its explicit specialist and adjudication upgrades. A profile is a routing policy, not a promise that unavailable models exist.

A plain “Run $super-review” uses Economy. Request separate specialists with “Run $super-review using the Balanced profile.” Economy changes reviewer count, not the required coverage or model capability.

### Economy dispatch

- Determine applicability per dimension before grouping. Launch one fresh, report-only reviewer for each non-empty configured group, normally at most four initial reviewers. Omit inapplicable dimension roles. Include historical context in the structure group even when its dimensions do not apply; include the mechanical prepass only when code quality applies. Do not spawn separate history or mechanical-prepass reviewers in Economy.
- Resolve each assigned role using the normal user/project/provider precedence. For a compatible group, use the highest required capability tier and reasoning effort among its assigned roles, then apply provider ceilings. Lower-tier roles may share that stronger reviewer; no role is downgraded to save cost. Record actual routing for each role.
- If explicit role-specific models, provider constraints, or a required independent specialist prevent sharing an invocation, split only the incompatible roles and disclose the extra invocations. If no eligible routing fits the user's ceiling, mark the affected roles `owed`; grouping does not override model choices or ceilings.
- Give each group a common factual packet: frozen target and acceptance criteria, applicable project instructions, relevant changed and adjacent paths, and collected deterministic evidence. Add all assigned role rubrics. Exclude builder rationale and other reviewers' conclusions. Reuse factual evidence, not another reviewer's judgments; inspect original source as needed.
- Every assigned dimension receives its own evidence, findings, unknowns, and status under `output-contract.md`. Group members share context and are not independent reviews of one another; reviewers remain independent of the builder and other groups. Keep historical and mechanical evidence separate from dimension conclusions, and preserve all eight rows in the final matrix.
- Keep consolidated adjudication in a separate fresh invocation when required. Never reuse a proposing reviewer as its own adjudicator. Avoid additional delegated extraction, rule-discovery, or citation helpers in Economy when the orchestrator or assigned group can perform that work.
- After repairs, apply the same grouping only to dimensions with accepted findings or materially affected scope. Use fresh verification contexts at the final SHA; include relevant helper work when affected, and carry unchanged passing lanes forward with their recorded basis. Do not rerun an unaffected dimension merely because it shared a group.

The documentation role defaults to `routine` capability with `high` reasoning and is launched only when documentation applies. When judging documentation depends on subtle security, payment, migration, concurrency, or distributed-system behavior, route the underlying factual question to the corresponding higher-capability specialist or consolidated adjudicator rather than silently upgrading documentation prose review into system adjudication.

## Claude role assignments

For a Claude review using the Balanced profile, resolve each role to the following model and agent. These are the Anthropic equivalents of the capability requirements in `reviewer-requirements.yml`; a generic request to use Claude uses these role mappings with the default Economy grouping, not one invocation per row.

| Role | Claude model | Native effort | Claude Code agent |
| --- | --- | --- | --- |
| `correctness` | `claude-opus-5` | `high` | `super-review-frontier-high` |
| `security` | `claude-opus-5` | `high` | `super-review-frontier-high` |
| `architecture` | `claude-opus-5` | `high` | `super-review-frontier-high` |
| `ui_accessibility` | `claude-opus-5` | `high` | `super-review-frontier-high` |
| `testing` | `claude-sonnet-5` | `high` | `super-review-advanced-high` |
| `code_quality` | `claude-sonnet-5` | `high` | `super-review-advanced-high` |
| `performance_reliability` | `claude-sonnet-5` | `high` | `super-review-advanced-high` |
| `historical_context` | `claude-sonnet-5` | `high` | `super-review-advanced-high` |
| `finding_adjudication` | `claude-sonnet-5` | `high` | `super-review-advanced-high` |
| `documentation` | `claude-haiku-4-5` | `high` | `super-review-routine-high` |
| `code_quality_mechanical_prepass` | `claude-haiku-4-5` | `high` | `super-review-routine-high` |
| `contract_extraction` | `claude-haiku-4-5` | `high` | `super-review-routine-high` |
| `rule_discovery` | `claude-haiku-4-5` | `high` | `super-review-routine-high` |
| `citation_validation` | `claude-haiku-4-5` | `high` | `super-review-routine-high` |
| `critical_finding_adjudication` | `claude-opus-5` | `high` | `super-review-frontier-high` |
| `synthesis` | `claude-opus-5` | `high` | Orchestrator; do not spawn another reviewer |

Balanced and Maximum give each specialist an independent invocation even when several roles use the same agent definition. Economy gives each compatible group one invocation using the agent that satisfies the strongest assigned role. Contract extraction, rule discovery, and citation validation are helper assignments when delegated, not additional mandatory reviewers. Use one separate adjudicator: ordinary or critical, as determined below.

Explicit current user choices and project overrides retain the resolution precedence above. Economy retains the Balanced role requirements and resolves grouped routing; Maximum recalculates its role requirements. Both apply the Anthropic high-effort ceiling before dispatch. `claude-opus-4-8` remains the configured frontier alternative; disclose a fallback when used. Claude CLI invocations must pass the resolved model and native effort explicitly, matching the model and effort bindings of the corresponding Claude Code agent.

## Escalation

Apply the `critical_finding_adjudication` role when a finding involves authentication, authorization, payments, secrets, sensitive data, irreversible writes, material data loss, concurrency, distributed state, public contracts, subtle financial/time invariants, or conflicting high-impact conclusions.

Do not escalate mechanical rule matching merely because the result is unpopular. Do not let a lower-tier reviewer make the final decision on a disputed high-impact finding.

Run the applicable specialists or Economy groups independently and in parallel when slots permit. Historical context has its own specialist in Balanced and Maximum and belongs to the structure group in Economy. Use one consolidated adjudicator only when material candidate findings exist. Do not add redundant backstop reviewers merely to increase reviewer count.
