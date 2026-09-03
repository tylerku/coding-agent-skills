#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install one skill from this checkout into Codex, Claude Code, or both."
    )
    parser.add_argument("skill", help="Skill directory name under skills/")
    parser.add_argument(
        "--host",
        choices=("codex", "claude", "both"),
        required=True,
        help="Personal skill directory to install into",
    )
    parser.add_argument(
        "--skills-directory",
        type=Path,
        help="Override the selected host's skills directory; unavailable with --host both",
    )
    parser.add_argument(
        "--claude-agents-directory",
        type=Path,
        help="Override Claude's agents directory when installing bundled agent definitions",
    )
    return parser.parse_args()


def destinations(host: str, override: Path | None) -> list[Path]:
    if override:
        if host == "both":
            raise SystemExit("--skills-directory cannot be combined with --host both")
        return [override.expanduser()]

    home = Path.home()
    codex_home = Path(os.environ.get("CODEX_HOME", home / ".codex"))
    resolved: list[Path] = []
    if host in ("codex", "both"):
        resolved.append(codex_home / "skills")
    if host in ("claude", "both"):
        resolved.append(home / ".claude" / "skills")
    return resolved


def claude_agents_root(args: argparse.Namespace) -> Path | None:
    if args.host not in ("claude", "both"):
        if args.claude_agents_directory:
            raise SystemExit("--claude-agents-directory requires --host claude or --host both")
        return None
    if args.claude_agents_directory:
        return args.claude_agents_directory.expanduser()
    if args.skills_directory:
        skills_directory = args.skills_directory.expanduser()
        is_project_claude_directory = (
            skills_directory.name == "skills" and skills_directory.parent.name == ".claude"
        )
        if not is_project_claude_directory:
            raise SystemExit(
                "Cannot infer Claude's agents directory from --skills-directory. "
                "Pass --claude-agents-directory explicitly."
            )
        return skills_directory.parent / "agents" / "coding-agent-skills"
    return Path.home() / ".claude" / "agents" / "coding-agent-skills"


def main() -> None:
    args = parse_args()
    if not SKILL_NAME.fullmatch(args.skill):
        raise SystemExit(f"Invalid skill name: {args.skill}")

    source = SKILLS_ROOT / args.skill
    if not (source / "SKILL.md").is_file():
        raise SystemExit(f"Unknown skill or missing SKILL.md: {args.skill}")

    roots = destinations(args.host, args.skills_directory)
    targets = [root / args.skill for root in roots]
    agent_source = source / "integrations" / "claude-code" / "agents"
    agent_root = claude_agents_root(args)
    agent_sources = sorted(agent_source.glob("*.md")) if agent_source.is_dir() else []
    agent_targets = [agent_root / path.name for path in agent_sources] if agent_root else []

    existing = [target for target in [*targets, *agent_targets] if target.exists()]
    if existing:
        paths = "\n".join(f"- {path}" for path in existing)
        raise SystemExit(
            "Refusing to overwrite existing skill directories. Preserve or remove them first:\n"
            f"{paths}"
        )

    for target in targets:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(source, target)
        print(f"Installed {args.skill} to {target}")

    for source_path, target in zip(agent_sources, agent_targets):
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target)
        print(f"Installed Claude agent {source_path.stem} to {target}")


if __name__ == "__main__":
    main()
