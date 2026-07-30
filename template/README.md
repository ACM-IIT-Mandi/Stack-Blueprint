# {{NAME}}

TODO: one sentence describing what this is.

> Work in progress, not ready to use yet.
> Delete this line once it actually runs (see docs/blueprint-guide.md).

## Overview

TODO: a short paragraph. What this is, and what kind of project it is a good starting point
for.

## Stack

| Layer | Choice |
| --- | --- |
| Language | TODO |
| Framework | TODO |
| Database | TODO |

## Prerequisites

- TODO: e.g. Python 3.12+
- Docker and Docker Compose
- `make` (on Windows, use WSL2 or Git Bash)

## Getting started

Every command below should work exactly as written, on a fresh clone.

### With Docker (recommended)

```bash
cp .env.example .env
make docker-up
```

The app will be at <http://localhost:{{PORT_BASE}}>.

### Without Docker

```bash
cp .env.example .env
make setup
make dev
```

## Commands

| Command | What it does |
| --- | --- |
| `make help` | List all commands |
| `make setup` | Install dependencies |
| `make dev` | Run locally |
| `make test` | Run tests |
| `make lint` | Check code style |
| `make format` | Fix code style |
| `make check` | Everything above at once, exactly what CI runs |
| `make docker-up` | Build and start everything |
| `make docker-down` | Stop everything |

## Configuration

Every setting is an environment variable. Copy `.env.example` to `.env` and fill it in.

| Variable | Required | Description |
| --- | --- | --- |
| `TODO` | yes | TODO |

## Testing

```bash
make test
```

TODO: anything worth knowing, like whether tests need Docker running.

## What's included

- ✅ TODO

Not included yet:

- ❌ TODO

## License

MIT, see the [repository LICENSE](../../../LICENSE). Use this for your own project freely.
