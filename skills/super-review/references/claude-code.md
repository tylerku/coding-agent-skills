# Claude Code Adapter

Invoke this skill as `/super-review` in Claude Code. The review contract, dimension rubrics, project overrides, severity rules, evidence requirements, and PR comment format remain unchanged.

## Specialist dispatch

- Use Claude Code's `Agent` tool for each applicable independent specialist and for consolidated adjudication when required. Use the installed `super-review-routine-high`, `super-review-advanced-high`, `super-review-frontier-high`, or `super-review-frontier-maximum` agent matching the resolved requirement.
- Use fresh, non-forked agent contexts so specialists do not inherit the builder's conversation or rationale. Supply the frozen contract and evidence described in the main skill explicitly because a Claude subagent does not inherit the parent conversation.
- Dispatch independent specialists in parallel when the available Agent interface supports parallel calls. Use bounded waves when concurrency is limited.
- The shipped Claude agents exclude `Agent`, `Skill`, and write/edit tools. Do not replace them with a generic agent unless another configured agent proves the same restrictions.
- Map `routine`, `advanced`, and `frontier` through `reviewer-models.yml`. The shipped agents bind the corresponding Anthropic model and native effort. A project-defined model may be passed per invocation only when the selected agent already enforces the required effort and restrictions.
- Treat any Claude Code model-substitution warning as a routing event. Accept it only when the actual substituted model is mapped at the same or a higher capability tier; otherwise mark the lane `owed`. Record the actual model and effort shown by the host receipt. When the active Claude Code surface cannot expose that receipt, disclose the limitation and do not claim exact routing compliance.
- If the Claude agent definitions are missing, stop before dispatch and report the affected lanes `owed` with installation instructions. Do not fall back silently to the general-purpose agent.

## Tools and publication

Use Claude Code's read/search/shell tools for repository evidence and an authenticated GitHub CLI or configured GitHub integration for PR resolution and the canonical informational comment. Tool availability never changes authorization: preserve the main skill's read-only source contract and request or honor publication permission exactly as specified.

The cross-host installer places the bundled definitions from `integrations/claude-code/agents/` in Claude Code's agent directory. `agents/openai.yaml` is ignored by Claude Code and may remain beside the portable skill without affecting discovery or execution.
