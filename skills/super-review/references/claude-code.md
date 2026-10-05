# Claude Code Adapter

Invoke this skill as `/super-review` in Claude Code. The review contract, dimension rubrics, project overrides, severity rules, evidence requirements, and PR comment format remain unchanged.

## Specialist dispatch

- Use Claude Code's `Agent` tool for each applicable independent specialist, or each compatible Economy group, and for separate consolidated adjudication when required. Economy groups use the strongest required model and effort among their assigned roles, following `model-routing.md`; do not lower capability or create separate invocations for grouped helper work. Select `super-review-routine-high` for routine roles and `super-review-advanced-high` for advanced roles (both bound to Sonnet 5.5), and `super-review-frontier-high` for Opus 5.5, including critical adjudication. The legacy `super-review-frontier-maximum` agent is a compatibility alias bound to Opus 5.5 at high effort.
- Use fresh, non-forked agent contexts so specialists do not inherit the builder's conversation or rationale. Supply the frozen contract and evidence described in the main skill explicitly because a Claude subagent does not inherit the parent conversation.
- Dispatch independent specialists in parallel when the available Agent interface supports parallel calls. Use bounded waves when concurrency is limited.
- The shipped Claude agents exclude `Agent`, `Skill`, and write/edit tools. Do not replace them with a generic agent unless another configured agent proves the same restrictions.
- Map `routine`, `advanced`, and `frontier` through `reviewer-models.yml`, applying its Anthropic `blocked_models` and `reasoning_effort_ceiling` first. Fable is disabled, and all Anthropic roles are capped at high effort, including critical adjudication and the Maximum profile. Project overrides cannot bypass this saved user preference. A project-defined model may be passed per invocation only when the selected agent enforces the effective effort and restrictions.
- Treat any Claude Code model-substitution warning as a routing event. Accept it only when the actual model is mapped at the same or a higher capability tier and respects the blocked-model list and high-effort ceiling; otherwise reroute to an eligible Opus agent or mark the lane `owed`. Record the actual model and effort shown by the host receipt. When the active Claude Code surface cannot expose that receipt, disclose the limitation and do not claim exact routing compliance.
- If the Claude agent definitions are missing, stop before dispatch and report the affected lanes `owed` with installation instructions. Do not fall back silently to the general-purpose agent.

## Tools and publication

Use Claude Code's read/search/shell tools for repository evidence and an authenticated GitHub CLI or configured GitHub integration for PR resolution and the canonical informational comment. Tool availability never changes authorization: preserve the main skill's read-only source contract and request or honor publication permission exactly as specified.

The cross-host installer places the bundled definitions from `integrations/claude-code/agents/` in Claude Code's agent directory. `agents/openai.yaml` is ignored by Claude Code and may remain beside the portable skill without affecting discovery or execution.
