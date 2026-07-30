# Repo tooling

Two small Python scripts. Neither is required reading, they just make a couple of things
easier.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

One dependency: PyYAML, so the scripts can read `blueprint.yaml` files.

## `new_blueprint.py`

Creates a new blueprint from the template folder.

```bash
python tools/new_blueprint.py --name fastapi-rest --category backend --steward @your-handle
```

It copies `template/` into `blueprints/<category>/<name>/`, fills in the name, category,
steward, and picks a free port block automatically.

## `check_blueprints.py`

The check GitHub Actions runs on every push and pull request. Makes sure every
`blueprint.yaml` is valid and the required files exist.

```bash
python tools/check_blueprints.py
```

It does not run a blueprint's own tests (`make test`), since blueprints can be in different
languages and there's no one runner that fits all of them. That's the blueprint's own
`Makefile`, and for now, its steward's job to run.

## `_common.py`

Small shared helpers the two scripts above use. Nothing here does anything on its own.
