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

## Profiles

Balanced is the default. Economy applies the explicit downgrades in `reviewer-requirements.yml`. Maximum applies its explicit specialist and adjudication upgrades. A profile is a routing policy, not a promise that unavailable models exist.

The documentation role defaults to `routine` capability with `high` reasoning and is launched only when documentation applies. When judging documentation depends on subtle security, payment, migration, concurrency, or distributed-system behavior, route the underlying factual question to the corresponding higher-capability specialist or consolidated adjudicator rather than silently upgrading documentation prose review into system adjudication.

## Escalation

Apply the `critical_finding_adjudication` role when a finding involves authentication, authorization, payments, secrets, sensitive data, irreversible writes, material data loss, concurrency, distributed state, public contracts, subtle financial/time invariants, or conflicting high-impact conclusions.

Do not escalate mechanical rule matching merely because the result is unpopular. Do not let a lower-tier reviewer make the final decision on a disputed high-impact finding.

Run the applicable dimension specialists and historical-context specialist independently and in parallel when slots permit. Use one consolidated adjudicator only when material candidate findings exist. Do not add redundant backstop reviewers merely to increase reviewer count.
