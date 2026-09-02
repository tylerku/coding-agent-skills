# Coding Agent Skills

A versioned collection of individually installable coding-agent skills.

## Available skills

| Skill | Description | Current release |
| --- | --- | --- |
| `pr-review` | Focused single-reviewer must-fix gate for open pull requests | `pr-review-v1.1.0` |
| `super-review` | Comprehensive, provider-neutral review of open GitHub pull requests | `super-review-v1.1.0` |
| `smoke-test` | Risk-scaled runtime feature challenges with edge cases and screenshot evidence | `smoke-test-v1.1.0` |

## Install one skill in Codex

Ask Codex:

> Use `$skill-installer` to install `super-review` from `https://github.com/tylerku/coding-agent-skills/tree/super-review-v1.1.0/skills/super-review`.

Or install the focused gate:

> Use `$skill-installer` to install `pr-review` from `https://github.com/tylerku/coding-agent-skills/tree/pr-review-v1.1.0/skills/pr-review`.

Or install the runtime journey tester:

> Use `$skill-installer` to install `smoke-test` from `https://github.com/tylerku/coding-agent-skills/tree/smoke-test-v1.1.0/skills/smoke-test`.

The repository is public, so the installer can download a skill without GitHub repository access. The skill becomes available on the next Codex turn after installation.

Each skill lives in a self-contained `skills/<skill-name>/` directory, so teammates can install only the skill they want. The standard installer will not overwrite an existing destination skill directory. Before upgrading, preserve or remove the existing installation deliberately, then install the desired release tag.

## Use super-review

Open a GitHub pull request, then ask:

> Run `$super-review` on PR #123 using the Balanced profile.

The skill requires exactly one matching open GitHub pull request. It reviews and reports only: it does not modify code, create a pull request, approve, request changes, or merge.

## Use smoke-test

Ask:

> Run `$smoke-test` on the affected critical journeys, capture every meaningful checkpoint on desktop and mobile, and publish the evidence to the matching PR if one exists.

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
