<div align="center">

# Stack Blueprint

**Clean, production-style starting points, so you stop rebuilding the same first weekend.**

A project by [ACM IIT Mandi](https://github.com/ACM-IIT-Mandi)

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

</div>

---

## The idea

If you have ever started a new project and spent the first weekend just setting things up,
folders, environment variables, Docker, tests, a linter, before writing a single feature,
that is exactly the part this repo tries to hand you already done.

Each folder under [`blueprints/`](blueprints/) is a small, working project in one stack:
FastAPI, Express, Next.js, and so on. Not a tutorial, not a huge feature-packed app. Just a
clean, sensible starting point: good folder structure, environment variables done properly,
logging, error handling, a few real tests, and Docker support.

We are also writing down, in plain language, *why* things are done a certain way, in
[`docs/standards.md`](docs/standards.md). Even if we don't have a blueprint in your favourite
stack yet, that file is worth a read on its own.

It is a learning project. We are students, building it as we go, and it is not finished.
That's the point.

## Where things stand right now

We're just getting started. The folders, docs, and template are ready, but there are no
finished blueprints yet. If you want to build the first one, see
[CONTRIBUTING.md](CONTRIBUTING.md).

## Use a blueprint

```bash
npx degit ACM-IIT-Mandi/Stack-Blueprint/blueprints/backend/<name> my-app
```

## What this is not

- Not a tutorial series
- Not a big feature-packed demo app (no dashboards, no shopping carts, no clones)
- Not mobile, desktop, or game development
- Not cloud-specific deployment scripts

The goal is a clean starting point, small enough to actually understand.

## Want to help?

Yes please. You don't need to be an expert yet, and you don't need to know GitHub already.

- Never used GitHub? Start with [REPO_GUIDE.md](REPO_GUIDE.md). It walks through every file
  here in plain language, and there's a glossary at the end.
- Ready to contribute? [CONTRIBUTING.md](CONTRIBUTING.md) is the whole process, and it's
  short.
- Looking for a first task? Check issues labelled `good-first-issue`.

Using AI tools is fine. Submitting code you can't explain is not. See
[AI_POLICY.md](AI_POLICY.md).

## Who runs this

See [MAINTAINERS.md](MAINTAINERS.md). Be nice to each other:
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## License

MIT. See [LICENSE](LICENSE). Use any blueprint as the base for your own project, personal or
commercial, no credit required (though we'd love to hear what you built).
