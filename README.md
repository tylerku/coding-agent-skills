# Super Review Skill

A provider-neutral Codex skill for comprehensive, evidence-backed review of open GitHub pull requests. It coordinates parallel quality specialists, historical-context review, consolidated finding adjudication, deterministic checks, and a stable pull-request comment format.

## Install in Codex

Ask Codex:

> Use `$skill-installer` to install `super-review` from `https://github.com/tylerku/super-review-skill/tree/v1.0.0/skills/super-review`.

The repository is private, so the installer needs GitHub credentials that can read it. The skill becomes available on the next Codex turn after installation.

The standard installer will not overwrite an existing `~/.codex/skills/super-review` directory. Before upgrading, preserve or remove the existing installation deliberately, then install the desired release tag.

## Use

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
skills/super-review/
├── SKILL.md
├── agents/openai.yaml
└── references/
```

## Development

Run the repository validator before opening a pull request:

```bash
python3 -m pip install pyyaml
python3 scripts/validate_skill.py
```

Publish stable revisions with semantic version tags so teammates can install a pinned version.
