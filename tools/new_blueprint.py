#!/usr/bin/env python3
"""Create a new blueprint from the template folder.

    python tools/new_blueprint.py --name fastapi-rest --category backend --steward @handle

This copies template/ into blueprints/<category>/<name>/ and fills in the basic details
(name, category, steward, a free port block). Open an approved blueprint proposal issue
first, that is what reserves the name so two people do not build the same thing.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _common import (  # noqa: E402
    BLUEPRINTS_DIR,
    CATEGORIES,
    NAME_RE,
    PORT_BLOCK_SIZE,
    STEWARD_RE,
    TEMPLATE_DIR,
    load_all_manifests,
    next_free_port_base,
    read_text,
    rel,
)

# Never copied out of the template folder.
EXCLUDE = {"TEMPLATE.md"}


def substitutions(name: str, category: str, steward: str, port_base: int) -> dict[str, str]:
    return {
        "{{NAME}}": name,
        "{{CATEGORY}}": category,
        "{{STEWARD}}": steward,
        "{{PORT_BASE}}": str(port_base),
        "{{PORT_BASE_PLUS_1}}": str(port_base + 1),
        "{{PORT_BASE_PLUS_9}}": str(port_base + PORT_BLOCK_SIZE - 1),
    }


def render_template(
    target: Path, *, name: str, category: str, steward: str, port_base: int
) -> list[Path]:
    """Copy template/ to target, filling in the placeholders. Returns files written."""
    if not TEMPLATE_DIR.is_dir():
        raise SystemExit(f"template folder not found at {TEMPLATE_DIR}")

    replacements = substitutions(name, category, steward, port_base)
    written: list[Path] = []

    for source in sorted(TEMPLATE_DIR.rglob("*")):
        relative = source.relative_to(TEMPLATE_DIR)
        if relative.parts[0] in EXCLUDE:
            continue

        destination = target / relative
        if source.is_dir():
            destination.mkdir(parents=True, exist_ok=True)
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        text = read_text(source)
        for placeholder, value in replacements.items():
            text = text.replace(placeholder, value)
        destination.write_text(text, encoding="utf-8")
        shutil.copymode(source, destination)
        written.append(destination)

    return written


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a new blueprint from the template")
    parser.add_argument("--name", required=True, help="kebab-case, e.g. fastapi-rest")
    parser.add_argument("--category", required=True, choices=CATEGORIES)
    parser.add_argument("--steward", required=True, help="your GitHub handle, e.g. @octocat")
    parser.add_argument(
        "--port-base",
        type=int,
        default=None,
        help="pick a specific port block instead of the next free one",
    )
    args = parser.parse_args()

    name: str = args.name
    steward: str = args.steward if args.steward.startswith("@") else f"@{args.steward}"

    if not NAME_RE.match(name):
        print(
            f"Name '{name}' should be lowercase with hyphens, like fastapi-rest or nextjs-app",
            file=sys.stderr,
        )
        return 1

    if not STEWARD_RE.match(steward):
        print(f"Steward '{steward}' should look like @your-handle", file=sys.stderr)
        return 1

    target = BLUEPRINTS_DIR / args.category / name
    if target.exists():
        print(f"{rel(target)} already exists", file=sys.stderr)
        return 1

    manifests = load_all_manifests()

    for _path, manifest in manifests:
        if manifest.get("name") == name:
            print(f"A blueprint named '{name}' already exists", file=sys.stderr)
            return 1

    taken = {
        m.get("ports", {}).get("base")
        for _p, m in manifests
        if isinstance(m.get("ports", {}).get("base"), int)
    }

    if args.port_base is not None:
        port_base = args.port_base
        if port_base in taken:
            print(f"Port block {port_base} is already used by another blueprint", file=sys.stderr)
            return 1
    else:
        free = next_free_port_base({t for t in taken if t is not None})
        if free is None:
            print("Every port block is taken, pick one manually with --port-base", file=sys.stderr)
            return 1
        port_base = free

    written = render_template(
        target, name=name, category=args.category, steward=steward, port_base=port_base
    )

    print(f"Created {rel(target)} ({len(written)} files)")
    print(f"Port block: {port_base}-{port_base + PORT_BLOCK_SIZE - 1}  Steward: {steward}\n")
    print("Next steps:")
    print(f"  1. Fill in {rel(target)}/blueprint.yaml (the stack fields are TODO)")
    print(f"  2. Fill in {rel(target)}/README.md")
    print("  3. Read docs/blueprint-guide.md and docs/standards.md as you build")
    print("\nYou do not have to finish everything today. Land a small draft and grow it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
