# Gate Output Contract

Return one structured result:

```json
{
  "schema_version": 1,
  "gate": "PASS",
  "check_conclusion": "success",
  "reviewer": {
    "provider": "configured-provider",
    "model": "configured-model",
    "capability_tier": "advanced",
    "reasoning_effort": "high"
  },
  "pull_request": {
    "repository": "owner/repository",
    "number": 123,
    "url": "https://github.com/owner/repository/pull/123",
    "head_sha": "full-sha",
    "base_sha": "full-sha",
    "head_ref": "feature-branch",
    "base_ref": "main"
  },
  "policy_sources": [
    {
      "source": "global:references/review-dimensions.md",
      "mode": "baseline",
      "dimensions": ["logical_correctness", "security", "architecture_style", "test_coverage", "documentation"]
    },
    {
      "source": "docs/code-review/review-policy.yml -> docs/code-review/architecture.md",
      "mode": "extend",
      "dimensions": ["architecture_style"]
    }
  ],
  "dimensions": {
    "logical_correctness": { "status": "pass", "summary": "..." },
    "security": { "status": "pass", "summary": "..." },
    "architecture_style": { "status": "pass", "summary": "..." },
    "test_coverage": { "status": "pass", "summary": "..." },
    "documentation": { "status": "not_applicable", "summary": "..." }
  },
  "must_fix": [],
  "warnings": [],
  "passed": [],
  "limitations": [],
  "reviewed_at": "2026-01-01T00:00:00Z"
}
```

Dimension status is `pass`, `findings`, `not_applicable`, or `blocked`.

Each finding contains:

```json
{
  "id": "LOGIC-1",
  "dimension": "logical_correctness",
  "severity": "must_fix",
  "confidence": 0.92,
  "location": { "path": "src/example.ts", "line": 42 },
  "basis": "Specific requirement or review rule",
  "proof": "Traced mechanism and triggering conditions",
  "impact": "Concrete consequence if merged",
  "smallest_fix": "Minimum appropriate correction"
}
```

Confidence estimates whether the factual claim is correct, not its severity:

- `0.50`: mechanism appears plausible but reachability or impact remains materially uncertain.
- `0.80`: mechanism and realistic reachability are supported strongly enough for a gate decision.
- `0.90`: deterministic evidence or a fully traced path strongly establishes the claim.
- `1.00`: reproduced directly or logically unavoidable under confirmed conditions.

Map gate to required-check conclusion:

- `PASS` -> `success`.
- `FAIL` -> `failure`.
- `BLOCKED` -> `failure`.
- `STALE` -> do not publish; cancel or supersede the stale run and review the new SHA.

Warnings never fail the check. `passed` contains concise evidence for dimensions that were actually examined; it is not a generic compliment list.
