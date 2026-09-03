# Specialist Output Contract

Each specialist returns one structured report with these fields:

```json
{
  "dimension": "architecture",
  "status": "pass",
  "reviewer": {
    "role": "architecture",
    "runner": "codex",
    "provider": "openai",
    "model": "gpt-5.6-sol",
    "capability_tier": "frontier",
    "reasoning_effort": "high",
    "native_reasoning_effort": "high",
    "fallback": null
  },
  "rubric_sources": ["global:references/architecture.md"],
  "scope_examined": ["src/example.ts"],
  "evidence": [
    {
      "kind": "code|test|command|runtime|documentation|history",
      "source": "path, command, or observation",
      "result": "concise observed result"
    }
  ],
  "findings": [],
  "unknowns": []
}
```

Dimension identifiers are `correctness`, `security`, `testing`, `architecture`, `code_quality`, `documentation`, `ui_accessibility`, and `performance_reliability`.

`status` must be one of:

- `pass`: examined with sufficient evidence and no findings.
- `findings`: one or more findings are present.
- `not_applicable`: the dimension does not apply, with a reason in `evidence`.
- `owed`: applicable evidence could not be collected in the current environment.
- `blocked`: the review cannot make a responsible judgment without a missing decision, contract, or required access.

Each finding contains:

```json
{
  "id": "ARCH-1",
  "title": "Short concrete title",
  "severity": "blocker|warning|improvement",
  "confidence": 0.0,
  "location": { "path": "src/example.ts", "line": 42 },
  "basis": "specific rubric rule or acceptance criterion",
  "proof": "why the issue is real and reachable",
  "impact": "observable consequence",
  "remediation": "smallest appropriate fix or decision",
  "scope": "in_scope|follow_up|escalate"
}
```

Specialists propose findings only. They do not decide whether the orchestrator may edit the PR. After adjudication, attach this lifecycle record to every accepted blocker and warning:

```json
{
  "finding_id": "ARCH-1",
  "first_seen_sha": "full initial SHA",
  "repair_disposition": "auto_fix|decision_required|repair_owed",
  "resolution_state": "fixed|open|decision_required|repair_owed",
  "disposition_reason": "why repair is safe, requires a decision, or is operationally owed",
  "repair_commit": "full final SHA or null",
  "repair_summary": "what changed or why no edit was made",
  "verification": ["command, specialist conclusion, or other exact evidence"]
}
```

Do not use `fixed` until the repair is pushed and verified on the PR's final SHA. Preserve the original finding ID and first-seen SHA even when the original line no longer exists.

Use `blocker` only when the current change cannot safely land. Use `warning` for a real, material quality problem that may be consciously accepted. Use `improvement` for worthwhile non-blocking refinement. Do not encode importance in confidence.

## Confidence anchors

`confidence` estimates whether the finding's factual claim is correct. It does not measure severity, impact, or how strongly the reviewer feels.

- `0.00`: disproven or unsupported; reject it.
- `0.25`: plausible hypothesis with no verified mechanism or reachability.
- `0.50`: mechanism is supported, but reachability, conditions, or impact remain materially uncertain.
- `0.75`: reachable and likely, supported by code and relevant context, but not directly demonstrated.
- `0.90`: strongly established by deterministic evidence, a focused test, or a fully traced unavoidable code path.
- `1.00`: reproduced directly or logically unavoidable under confirmed conditions.

Use intermediate values only when the evidence genuinely falls between anchors. Do not discard a severe low-confidence concern solely because of its score; route it to adjudication or record it as unresolved uncertainty.

Findings must cite changed code or a directly affected contract. Avoid style preferences without a rubric basis, speculative scale concerns without a plausible mechanism, and recommendations whose complexity exceeds their benefit.

## Final matrix status

Specialist statuses describe their raw report. After consolidated adjudication and evidence reconciliation, recompute the final dimension status using this precedence:

1. `blocked` when a missing decision, target, effective rubric, or required access prevents a responsible conclusion.
2. `owed` when the dimension is applicable but required evidence could not be collected.
3. `decision_required` when an accepted finding cannot be resolved without a human decision.
4. `findings` when another accepted finding remains unresolved.
5. `pass_after_fixes` when accepted findings were verified fixed on the final SHA and none remain unresolved.
6. `pass` when evidence is sufficient and no accepted finding was established.
7. `not_applicable` only when the dimension truly does not apply.

A higher-precedence status does not hide accepted findings; list them alongside the status. If all proposed findings are rejected and no evidence debt remains, report `pass`. Fixed findings remain in the lifecycle report but do not make the final lane `findings`.

`unknowns` records limitations outside the source-review contract, including missing runtime or screenshot evidence. Their presence does not automatically make a source-review lane `owed`; use `owed` only when evidence required to judge the source change itself could not be collected.
