#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
FRONTMATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
MARKDOWN_LINK = re.compile(r"\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> object:
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        fail(f"{path.relative_to(ROOT)}: {error}")


def discover_skills() -> list[Path]:
    if not SKILLS_ROOT.is_dir():
        fail("skills directory is missing")
    skills = sorted(path for path in SKILLS_ROOT.iterdir() if (path / "SKILL.md").is_file())
    if not skills:
        fail("no skill directories containing SKILL.md were found")
    return skills


def validate_entrypoint(skill: Path) -> None:
    entrypoint = skill / "SKILL.md"
    text = entrypoint.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail(f"{entrypoint.relative_to(ROOT)} must start with YAML frontmatter")

    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        fail(f"{entrypoint.relative_to(ROOT)} frontmatter must be a mapping")
    if metadata.get("name") != skill.name:
        fail(f"{entrypoint.relative_to(ROOT)} name must match its directory: {skill.name}")
    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
        fail(f"{entrypoint.relative_to(ROOT)} requires a non-empty description")


def validate_yaml_files(skill: Path) -> None:
    yaml_paths = sorted(skill.rglob("*.yml")) + sorted(skill.rglob("*.yaml"))
    for path in yaml_paths:
        load_yaml(path)


def validate_local_links(skill: Path) -> None:
    for markdown_path in sorted(skill.rglob("*.md")):
        text = markdown_path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "#", "{{")):
                continue
            clean_target = target.split("#", 1)[0]
            resolved = (markdown_path.parent / clean_target).resolve()
            try:
                resolved.relative_to(skill.resolve())
            except ValueError:
                fail(f"{markdown_path.relative_to(ROOT)} links outside its skill: {target}")
            if not resolved.exists():
                fail(f"{markdown_path.relative_to(ROOT)} has a missing link: {target}")


def validate_no_scaffolding(skill: Path) -> None:
    markers = ("TODO", "FIXME", "[TODO:")
    for path in sorted(skill.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker in text:
                fail(f"{path.relative_to(ROOT)} contains unfinished marker {marker}")


def main() -> None:
    skills = discover_skills()
    for skill in skills:
        validate_entrypoint(skill)
        validate_yaml_files(skill)
        validate_local_links(skill)
        validate_no_scaffolding(skill)
        print(f"validated {skill.relative_to(ROOT)}")
    print(f"{len(skills)} skill(s) passed validation")


if __name__ == "__main__":
    main()
