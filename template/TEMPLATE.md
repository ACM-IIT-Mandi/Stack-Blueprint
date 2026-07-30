# About this folder

This is the blank starting point every new blueprint is copied from. Do not copy it by hand,
use the script, it fills in the name, steward, and a free port block for you, and skips this
file:

```bash
python tools/new_blueprint.py --name fastapi-rest --category backend --steward @your-handle
```

## What is in here

| File | What to do with it |
| --- | --- |
| `blueprint.yaml` | Already filled in. Update `features` as things start working. |
| `README.md` | Replace every `TODO`. |
| `ARCHITECTURE.md` | Not needed right away, write it once things are working, it is much easier to write while it is fresh in your head. |
| `Makefile` | Fill in the commands. Keep the names as they are. |
| `.env.example` | List every setting your app reads, fake values only. |
| `Dockerfile`, `docker-compose.yml` | Commented skeletons, replace with a real setup for your stack. |
| `src/`, `tests/` | Rename `src/` to `app/` if that fits your stack better. |

## While you build

- [docs/blueprint-guide.md](../docs/blueprint-guide.md), the steps in order
- [docs/standards.md](../docs/standards.md), how to do each part well

Land something small early and keep improving it. That is easier than trying to make it
perfect before anyone sees it, and it is how you get help.

## Changing this template

Changes here affect every blueprint made after that. If you are thinking about changing it,
mention it in an issue first so a maintainer can weigh in.
