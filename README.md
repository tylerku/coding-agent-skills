# Coding Agent Skills

A versioned collection of individually installable coding-agent skills.

The workflow definitions follow the shared Agent Skills `SKILL.md` format and include host adapters for Codex and Claude Code. Host-specific interface metadata is optional and never changes the underlying review or test contract.

## Available skills

| Skill | Description | Current release |
| --- | --- | --- |
| `pr-review` | Focused single-reviewer must-fix gate for open pull requests | `pr-review-v1.2.1` |
| `super-review` | Comprehensive, provider-neutral review and repair of open GitHub pull requests | `super-review-v1.3.1` |
| `smoke-test` | Risk-scaled runtime feature challenges with edge cases and screenshot evidence | `smoke-test-v1.3.0` |

## Install one skill in Codex

Ask Codex:

> Use `$skill-installer` to install `super-review` from `https://github.com/tylerku/coding-agent-skills/tree/super-review-v1.3.1/skills/super-review`.

Or install the focused gate:

> Use `$skill-installer` to install `pr-review` from `https://github.com/tylerku/coding-agent-skills/tree/pr-review-v1.2.1/skills/pr-review`.

Or install the runtime journey tester:

> Use `$skill-installer` to install `smoke-test` from `https://github.com/tylerku/coding-agent-skills/tree/smoke-test-v1.3.0/skills/smoke-test`.

The repository is public, so the installer can download a skill without GitHub repository access. The skill becomes available on the next Codex turn after installation.

## Install one skill in Claude Code

Claude Code discovers personal skills under `~/.claude/skills/` and invokes them with slash commands. Check out the release you want, then use the repository installer so only the selected skill is copied:

```bash
git clone --depth 1 --branch super-review-v1.3.1 https://github.com/tylerku/coding-agent-skills.git
cd coding-agent-skills
python3 scripts/install_skill.py super-review --host claude
```

Replace the tag and skill name with `pr-review-v1.2.1` / `pr-review` or `smoke-test-v1.3.0` / `smoke-test` as needed. The installer refuses to overwrite an existing skill or bundled Claude agent definition. Before upgrading, preserve or remove the old skill directory and any associated definitions under `~/.claude/agents/coding-agent-skills/`. Claude Code detects additions inside existing personal skills and agents directories live. Restart Claude Code when either top-level directory did not exist when the session started.

The same installer can install a checked-out release into Codex with `--host codex`, or both personal skill directories with `--host both`. When a skill bundles Claude Code subagents, the installer places those definitions under `~/.claude/agents/coding-agent-skills/` and refuses to overwrite an existing definition.

For a project-scoped Claude Code installation, copy into that repository's `.claude/skills/` directory instead:

```bash
python3 scripts/install_skill.py super-review --host claude --skills-directory /path/to/project/.claude/skills
```

Each skill lives in a self-contained `skills/<skill-name>/` directory, so teammates can install only the skill they want. Neither installer overwrites an existing destination skill directory. Before upgrading, preserve or remove the existing installation deliberately, then install the desired release tag.

## Use super-review

Open a GitHub pull request, then ask:

> Run `$super-review` on PR #123 using the Balanced profile.

In Claude Code, invoke the same workflow with:

> `/super-review PR #123 using the Balanced profile`

The skill requires exactly one matching open GitHub pull request. By default, an explicit run repairs clear accepted blockers and warnings in one bounded wave, verifies and pushes the repair to the unchanged PR head, and reports fixed versus unresolved findings. It does not create a pull request, force-push, approve, request changes, deploy, or merge. Ask for `report-only` behavior when no source changes are wanted.

## Use pr-review

Run the focused gate in a cold independent task. In Codex:

> Run `$pr-review` on PR #123.

In Claude Code:

> `/pr-review PR #123`

## Use smoke-test

Ask:

> Run `$smoke-test` on the affected critical journeys, capture every meaningful checkpoint on desktop and mobile, and publish the evidence to the matching PR if one exists.

In Claude Code, invoke the same workflow with:

> `/smoke-test Test the affected critical journeys, capture every meaningful checkpoint on desktop and mobile, and publish the evidence to the matching PR if one exists.`

The skill does not require a pull request. It runs against the application, reports screenshot-backed observations in the session, and publishes a canonical informational PR comment only when the tested checkout is clean and exactly matches the PR head.

## Project-specific rules

Keep reusable review principles in the global skill. Each project may extend them with:

- `docs/code-review/review-policy.yml`
- `docs/code-review/reviewers.yml`
- linked rubric files under `docs/code-review/`

Project review definitions extend the global rubrics by default. Replacement must be explicit.

Projects may optionally define smoke-test journeys and runtime instructions under `docs/smoke-test/`. Smoke-test project definitions also extend the global defaults unless replacement is explicit.

## Repository structure

```text
skills/
├── pr-review/
├── smoke-test/
└── super-review/
```

Every skill must remain self-contained: its local links and required resources cannot escape its own directory. Add future skills as sibling directories under `skills/`.

## Development

Run the repository validator before opening a pull request:

```bash
python3 -m pip install pyyaml
python3 scripts/validate_skills.py
```

Publish stable revisions with skill-specific tags such as `super-review-v1.0.0` so teammates can install a pinned version without coupling every skill's release cadence.
