# Building a blueprint

The practical guide: what files a blueprint needs, and the steps in order. For the reasoning
behind the folder layout, see
[docs/ARCHITECTURE.md](ARCHITECTURE.md). For how to write good code once you're in there, see
[docs/standards.md](standards.md).

If you are about to start your first blueprint, read this file once. It is not long.

## What is inside a blueprint folder

```
blueprints/backend/fastapi-rest/
  blueprint.yaml       what this is, and how far along it is
  README.md            how to run it, and what it includes
  ARCHITECTURE.md      why it is built this way (write this once it works)
  Makefile             setup / dev / test / lint / format / check / docker-up / docker-down
  .env.example         every setting, with fake values
  Dockerfile
  docker-compose.yml
  src/ (or app/)       the code
  tests/
```

`blueprint.yaml`, in plain terms:

```yaml
name: fastapi-rest
category: backend
summary: "A FastAPI REST service with logging, config, and Docker."
steward: "@your-handle"   # who looks after this one
ports:
  base: 8010              # your own block of 10 ports, so blueprints never clash
  allocated: [8010, 8011]
features:                 # only list what actually works right now
  - logging
  - docker
```

`features` is the one field people will actually read. If it says `testing` and there are no
tests, that is the fastest way to lose everyone's trust in the whole repo. Only add something
to the list once it genuinely works.

## The steps in order

1. **Open a "New blueprint" issue** and wait for a thumbs up. Usually takes a day, and it
   just stops two people building the same thing.
2. **Branch:** `git checkout -b blueprint/fastapi-rest`
3. **Create the folder from the template:**
   ```bash
   python tools/new_blueprint.py --name fastapi-rest --category backend --steward @your-handle
   ```
   This fills in the manifest and picks you a free port block automatically.
4. **Get it running.** Fill in the Makefile, Dockerfile, and `.env.example` for real, then
   make sure `make setup` and `make dev` actually work on a fresh clone.
5. **Add real tests**, following [docs/standards.md](standards.md). `make test` should pass.
6. **Write the README**, replacing every `TODO`. The "Getting started" section has to work
   exactly as written, on a machine that has never seen this project.
7. **Update `blueprint.yaml`'s `features` list** to match what you actually built.
8. **Add a row to [`blueprints/README.md`](../blueprints/README.md)** in the same pull
   request.
9. Run `make check`, then open the pull request.

You do not have to do all nine steps in one pull request. Landing something small after step
4 or 5 and improving it later is completely normal, and often the easier way to get help.


## Keeping it alive

Blueprints sometimes stop working for reasons that have nothing to do with the code itself, a
framework puts out a new major version, a base Docker image changes. Nobody's watching this
automatically yet since there are no blueprints to watch, so for now it is on the steward to
notice, roughly when touching the blueprint for something else or when someone opens an
issue about it. Once the first few blueprints exist, adding a small CI check scoped to that
blueprint's own folder is a good idea, and its steward is the right person to add it.

**Moving on is completely normal.** People graduate, get busy, lose interest in a stack. If
you can no longer look after your blueprint:

1. Open an issue saying so, and what state it's in.
2. A maintainer finds someone else, or marks it as needing a new steward.

Nothing gets deleted. The code stays exactly where it is, and anyone can pick it back up.

## Quick checklist before opening a pull request

- [ ] `make check` passes on your machine
- [ ] You ran it from a genuinely fresh clone at least once
- [ ] `blueprint.yaml`'s `features` list matches what actually works
- [ ] No `.env` file committed, no real secrets anywhere
- [ ] Nothing in your blueprint reads from, or copies from, outside its own folder
