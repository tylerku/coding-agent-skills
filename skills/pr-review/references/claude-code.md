# Claude Code Adapter

Invoke this skill as `/pr-review` in Claude Code. The five-dimension gate, confidence threshold, project overrides, decision states, and output contract remain unchanged.

The invocation itself must be the one cold independent reviewer. Run it in a fresh Claude Code task, CI agent invocation, or other context that did not build the change. Do not launch another subagent from inside the review; that would turn the single-reviewer gate into an orchestrated review and overlap with `super-review`.

Use Claude Code's read/search/shell tools for repository evidence and an authenticated GitHub CLI or configured GitHub integration for PR resolution and authorized publication. Resolve `advanced` to Sonnet and `frontier` to Opus through `reviewer-models.yml`, then run the cold review task with `high` effort. Fable is not an automatic PR-gate route; use it only when the user explicitly requests it or project policy both maps it and sets `allow_premium_fable: true`. Treat a model-substitution warning as a routing event: accept the actual model only when it maps to the same or a higher capability tier and, if it is Fable, the premium authorization rule also passes. Otherwise reroute to an eligible Sonnet or Opus reviewer, or return `BLOCKED` rather than silently changing cost or capability. Record the actual model in the reviewer receipt.

`agents/openai.yaml` is ignored by Claude Code. It may remain beside the portable skill without affecting discovery or execution.
