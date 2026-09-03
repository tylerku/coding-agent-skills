# Claude Code Adapter

Invoke this skill as `/smoke-test` in Claude Code. The risk model, journey selection, evidence rules, canonical report, and PR publication contract remain unchanged.

## Runtime control and evidence

- Use the repository's existing end-to-end harness when available; otherwise control Playwright or another reproducible browser driver through Claude Code's shell tools.
- Keep one journey controller in the main skill invocation. Do not distribute steps from one stateful journey across parallel subagents.
- Capture screenshots to stable absolute paths and attach or render them in the Claude Code session when the active surface supports images. Always include the artifact path or authorized URL in the canonical checkpoint.
- A surface that cannot render images does not waive evidence. Preserve every screenshot artifact and mark session delivery `OWED` when the complete required visual evidence is not accessible from that session.
- Use an authenticated GitHub CLI or configured GitHub integration for PR resolution and authorized comment publication. Upload screenshots only through the project's authorized artifact mechanism before embedding them in a PR.

Tool availability never broadens authority to mutate production, trigger external side effects, overwrite test data, or publish sensitive screenshots.

`agents/openai.yaml` is ignored by Claude Code. It may remain beside the portable skill without affecting discovery or execution.
