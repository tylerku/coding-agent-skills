# Coding Agent Skills

A versioned collection of individually installable coding-agent skills.

## Available skills

| Skill | Description | Current release |
| --- | --- | --- |
| `pr-review` | Focused single-reviewer must-fix gate for open pull requests | `pr-review-v1.1.0` |
| `super-review` | Comprehensive, provider-neutral review of open GitHub pull requests | `super-review-v1.1.0` |

## Install one skill in Codex

Ask Codex:

> Use `$skill-installer` to install `super-review` from `https://github.com/tylerku/coding-agent-skills/tree/super-review-v1.1.0/skills/super-review`.

Or install the focused gate:

> Use `$skill-installer` to install `pr-review` from `https://github.com/tylerku/coding-agent-skills/tree/pr-review-v1.1.0/skills/pr-review`.

The repository is private, so the installer needs GitHub credentials that can read it. The skill becomes available on the next Codex turn after installation.

Each skill lives in a self-contained `skills/<skill-name>/` directory, so teammates can install only the skill they want. The standard installer will not overwrite an existing destination skill directory. Before upgrading, preserve or remove the existing installation deliberately, then install the desired release tag.

## Use super-review

Open a GitHub pull request, then ask:

> Run `$super-review` on PR #123 using the Balanced profile.

The skill requires exactly one matching open GitHub pull request. It reviews and reports only: it does not modify code, create a pull request, approve, request changes, or merge.

## Project-specific rules

Keep reusable review principles in the global skill. Each project may extend them with:

- `docs/code-review/review-policy.yml`
- `docs/code-review/reviewers.yml`
- linked rubric files under `docs/code-review/`

Project review definitions extend the global rubrics by default. Replacement must be explicit.

## Repository structure

```text
skills/
├── pr-review/
│   ├── SKILL.md
│   ├── agents/openai.yaml
│   └── references/
└── super-review/
    ├── SKILL.md
    ├── agents/openai.yaml
    └── references/
```

Every skill must remain self-contained: its local links and required resources cannot escape its own directory. Add future skills as sibling directories under `skills/`.

## Development

Run the repository validator before opening a pull request:

```bash
python3 -m pip install pyyaml
python3 scripts/validate_skills.py
```

Publish stable revisions with skill-specific tags such as `super-review-v1.0.0` so teammates can install a pinned version without coupling every skill's release cadence.
