#!/usr/bin/env python3
"""A light structural check, this is what CI runs.

    python tools/check_blueprints.py

For every blueprint folder, checks that blueprint.yaml is valid and has the fields we need,
and that the required files exist. It does not run the blueprint's own tests, that is up to
whoever built it, since blueprints can be in any language and there's no single test runner
that fits all of them.

Exit code 0 if everything is fine, 1 if something is missing or wrong.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    CATEGORIES,
    NAME_RE,
    PORT_BASE_MAX,
    PORT_BASE_MIN,
    PORT_BLOCK_SIZE,
    STEWARD_RE,
    ManifestError,
    discover_blueprints,
    load_manifest,
    rel,
)

REQUIRED_FILES = ["blueprint.yaml", "README.md", "Makefile", ".gitignore"]


def check_one(path: Path) -> list[str]:
    """Return a list of problems found for this blueprint. Empty means it's fine."""
    problems: list[str] = []

    for name in REQUIRED_FILES:
        if not (path / name).is_file():
            problems.append(f"missing required file: {name}")

    try:
        manifest = load_manifest(path)
    except ManifestError as exc:
        problems.append(str(exc))
        return problems

    name = manifest.get("name")
    if not isinstance(name, str) or not NAME_RE.match(name):
        problems.append(f"name should be lowercase with hyphens, got {name!r}")
    elif name != path.name:
        problems.append(f"name '{name}' doesn't match the folder name '{path.name}'")

    category = manifest.get("category")
    if category not in CATEGORIES:
        problems.append(f"category must be one of {list(CATEGORIES)}, got {category!r}")
    elif category != path.parent.name:
        problems.append(f"category '{category}' doesn't match the parent folder")

    steward = manifest.get("steward")
    if not isinstance(steward, str) or not STEWARD_RE.match(steward):
        problems.append(f"steward should look like @handle, got {steward!r}")

    ports = manifest.get("ports") or {}
    base = ports.get("base")
    if not isinstance(base, int) or isinstance(base, bool):
        problems.append("ports.base must be a number")
    else:
        if base % PORT_BLOCK_SIZE != 0 or not (PORT_BASE_MIN <= base <= PORT_BASE_MAX):
            problems.append(
                f"ports.base {base} should be a multiple of 10 between "
                f"{PORT_BASE_MIN} and {PORT_BASE_MAX}"
            )
        allocated = ports.get("allocated") or []
        for port in allocated:
            if not (base <= port < base + PORT_BLOCK_SIZE):
                problems.append(f"port {port} is outside this blueprint's own block")

    if not isinstance(manifest.get("features"), list):
        problems.append("features must be a list (use [] if there's nothing yet)")

    return problems


def check_no_port_clashes(blueprints: list[Path]) -> list[str]:
    """No two blueprints should claim the same port block."""
    problems: list[str] = []
    seen: dict[int, str] = {}
    for path in blueprints:
        try:
            manifest = load_manifest(path)
        except ManifestError:
            continue
        base = (manifest.get("ports") or {}).get("base")
        if not isinstance(base, int):
            continue
        if base in seen:
            problems.append(f"port block {base} is used by both {seen[base]} and {path.name}")
        else:
            seen[base] = path.name
    return problems


def main() -> int:
    blueprints = discover_blueprints()

    if not blueprints:
        print("No blueprints yet, nothing to check.")
        return 0

    failed = False
    for path in blueprints:
        problems = check_one(path)
        if problems:
            failed = True
            print(f"{rel(path)}")
            for problem in problems:
                print(f"  - {problem}")
        else:
            print(f"{rel(path)}: ok")

    for problem in check_no_port_clashes(blueprints):
        failed = True
        print(problem)

    if failed:
        print("\nSomething needs fixing above. See docs/blueprint-guide.md.")
        return 1

    print(f"\nAll {len(blueprints)} blueprint(s) look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
