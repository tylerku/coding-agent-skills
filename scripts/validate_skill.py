#!/usr/bin/env python3

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "super-review"
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


def validate_entrypoint() -> None:
    entrypoint = SKILL / "SKILL.md"
    if not entrypoint.is_file():
        fail("skills/super-review/SKILL.md is missing")

    text = entrypoint.read_text(encoding="utf-8")
    match = FRONTMATTER.match(text)
    if not match:
        fail("SKILL.md must start with YAML frontmatter")

    metadata = yaml.safe_load(match.group(1))
    if not isinstance(metadata, dict):
        fail("SKILL.md frontmatter must be a mapping")
    if metadata.get("name") != "super-review":
        fail("SKILL.md name must be super-review")
    if not isinstance(metadata.get("description"), str) or not metadata["description"].strip():
        fail("SKILL.md requires a non-empty description")


def validate_yaml_files() -> None:
    yaml_paths = sorted(SKILL.rglob("*.yml")) + sorted(SKILL.rglob("*.yaml"))
    for path in yaml_paths:
        load_yaml(path)


def validate_local_links() -> None:
    for markdown_path in sorted(SKILL.rglob("*.md")):
        text = markdown_path.read_text(encoding="utf-8")
        for target in MARKDOWN_LINK.findall(text):
            if target.startswith(("http://", "https://", "#", "{{")):
                continue
            clean_target = target.split("#", 1)[0]
            resolved = (markdown_path.parent / clean_target).resolve()
            try:
                resolved.relative_to(SKILL.resolve())
            except ValueError:
                fail(f"{markdown_path.relative_to(ROOT)} links outside the skill: {target}")
            if not resolved.exists():
                fail(f"{markdown_path.relative_to(ROOT)} has a missing link: {target}")


def validate_no_scaffolding() -> None:
    markers = ("TODO", "FIXME", "[TODO:")
    for path in sorted(SKILL.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker in text:
                fail(f"{path.relative_to(ROOT)} contains unfinished marker {marker}")


def main() -> None:
    validate_entrypoint()
    validate_yaml_files()
    validate_local_links()
    validate_no_scaffolding()
    print("super-review skill validation passed")


if __name__ == "__main__":
    main()
