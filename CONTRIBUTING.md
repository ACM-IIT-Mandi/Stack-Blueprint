# Contributing

Welcome. This page is the whole process, it should take a few minutes to read.

If anything here is confusing, that's our fault, not yours. Open an issue and say so.

## The only rule that matters

**You should be able to explain what you submitted.**

Not perfectly, and not on the first try. But if a reviewer asks "why did you do it this
way?", you should have an answer. Using AI tools is completely fine, see
[AI_POLICY.md](AI_POLICY.md).

## First time contributing to anything?

That's fine, and this is a good place to start.

1. Read [REPO_GUIDE.md](REPO_GUIDE.md) if GitHub itself is new to you.
2. Ask questions. Asking early is normal here, not a sign you're struggling.

**Adding a new blueprint?** Open a "New blueprint" issue first and wait for a thumbs up.
Usually takes a day, and it's only there so two people don't build the same thing in the same
week.

## How to submit work

1. Make a branch: `git checkout -b blueprint/fastapi-rest` (or `fix/...`, `docs/...`).
2. Write your change. For a new blueprint, the steps are in
   [docs/blueprint-guide.md](docs/blueprint-guide.md).
3. Check it before pushing:
   ```bash
   make check
   ```
4. Push and open a pull request. Fill in the template, especially the part asking you to
   explain your work in your own words.
5. Wait for review. Expect questions, questions aren't criticism.

Open a **draft** pull request early if you want feedback partway through. We'd rather help
you at 50% than have you redo things at 100%.

## Keep in mind

- **Do not commit a real `.env` file**, or any real secret, anywhere, ever. `.env.example`
  only, with fake values.
- **One blueprint per pull request.** Blueprints are meant to be independent of each other,
  mixing two in one PR makes that harder to review.
- **Keep the `features` list in `blueprint.yaml` honest.** Only list something once it
  actually works. This is the single fastest way to lose people's trust in the repo.
- **Use your ecosystem's own defaults** for formatting and linting (Ruff or Black for Python,
  Prettier for JavaScript, and so on). Don't spend an evening tuning line length.

## Reporting a bug

Open a bug report with the exact steps that show the problem. A few commands beat a few
paragraphs of description.

## Questions

Open a [Discussion](https://github.com/ACM-IIT-Mandi/Stack-Blueprint/discussions), or ask in
the ACM channels. Nobody here will mind a basic question.

Everything you do here is covered by our [Code of Conduct](CODE_OF_CONDUCT.md).
