"""Small shared helpers used by the scripts in this folder.

Nothing fancy here on purpose. If you are reading this to understand the repo, the two
files that actually do things are new_blueprint.py (creates a blueprint) and
check_blueprints.py (the structural sanity check CI runs).
"""

from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    raise SystemExit(
        "PyYAML is not installed.\n\n    pip install -r tools/requirements.txt\n"
    )

REPO_ROOT = Path(__file__).resolve().parent.parent
BLUEPRINTS_DIR = REPO_ROOT / "blueprints"
TEMPLATE_DIR = REPO_ROOT / "template"

CATEGORIES = ("backend", "frontend", "fullstack")

NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
STEWARD_RE = re.compile(r"^@[A-Za-z0-9][A-Za-z0-9-]*$")

PORT_BASE_MIN = 8010
PORT_BASE_MAX = 8990
PORT_BLOCK_SIZE = 10


class ManifestError(Exception):
    """The manifest could not be read."""


def load_manifest(blueprint_dir: Path) -> dict[str, Any]:
    manifest_path = blueprint_dir / "blueprint.yaml"
    if not manifest_path.is_file():
        raise ManifestError(f"{rel(manifest_path)} does not exist")
    try:
        data = yaml.safe_load(manifest_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        raise ManifestError(f"{rel(manifest_path)} is not valid YAML: {exc}") from exc
    if not isinstance(data, dict):
        raise ManifestError(f"{rel(manifest_path)} must contain a YAML mapping")
    return data


def discover_blueprints() -> list[Path]:
    """Every folder under blueprints/<category>/ that has a blueprint.yaml."""
    found: list[Path] = []
    if not BLUEPRINTS_DIR.is_dir():
        return found
    for category in CATEGORIES:
        category_dir = BLUEPRINTS_DIR / category
        if not category_dir.is_dir():
            continue
        for entry in sorted(category_dir.iterdir()):
            if entry.is_dir() and (entry / "blueprint.yaml").is_file():
                found.append(entry)
    return found


def load_all_manifests() -> list[tuple[Path, dict[str, Any]]]:
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in discover_blueprints():
        try:
            out.append((path, load_manifest(path)))
        except ManifestError:
            continue
    return out


def rel(path: Path) -> str:
    """Path relative to the repo root, for readable messages."""
    for candidate in (Path(os.path.abspath(path)), path.resolve()):
        try:
            return str(candidate.relative_to(REPO_ROOT))
        except ValueError:
            continue
    return str(path)


def next_free_port_base(taken: set[int]) -> int | None:
    for base in range(PORT_BASE_MIN, PORT_BASE_MAX + 1, PORT_BLOCK_SIZE):
        if base not in taken:
            return base
    return None


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return ""
