# Why the folders are laid out this way

Quick read, worth it before you move anything around.

## The one big idea

**One blueprint, one folder. Everything about it lives there.**

The code, the config, the Dockerfile, the tests, and the README for a FastAPI blueprint all
sit inside `blueprints/backend/fastapi-rest/`. Nothing about it lives anywhere else, and it
does not reach into any other folder in this repo.

This means:

- You can copy that one folder out and start a real project from it, nothing else is needed
- A reviewer can see your whole contribution in one place
- If something is missing (no tests yet, no Docker support yet), it is obviously missing, a
  gap in one folder, not a mystery spread across the project


**Rule: a blueprint cannot depend on another blueprint, ever.** Not even a shared config
file, not even a shared "core" helper. This is stricter than it might need to be, but it is
what makes "copy the folder out and it just works" actually true, and it means a Python
blueprint and a Go blueprint sitting next to each other in this repo never has to make sense
to either the Python or the Go tooling.

This is a bit different from a normal codebase, where shared code between similar parts is
usually a good idea. Here it is not, on purpose, because each blueprint is meant to leave
this repo one day and become someone's real project. Sharing code across blueprints would
mean the thing you copy out quietly depends on a repo it is no longer part of.

## What every blueprint has in common

Not shared code, just a shared set of command names, so someone who has never touched your
stack can still run it:

```
make setup   make dev   make test   make lint   make format   make check
make docker-up   make docker-down
```

Same names everywhere, completely different scripts underneath. See
[docs/blueprint-guide.md](blueprint-guide.md) for what each one should do.

## Ports

Each blueprint reserves its own block of 10 host ports (so several blueprints can run side by
side on one laptop without clashing over the same port). This lives in `blueprint.yaml` and
is explained in [docs/blueprint-guide.md](blueprint-guide.md).
