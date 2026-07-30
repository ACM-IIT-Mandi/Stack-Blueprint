# What every file here is for

New to GitHub? This page walks through the whole project folder by folder, in plain
language. There's a glossary of common terms at the bottom too.

## The fast version

| You want to | Open |
| --- | --- |
| Understand the project | `README.md` |
| Contribute something | `CONTRIBUTING.md` |
| Build a blueprint | `docs/blueprint-guide.md` |
| Understand why it's laid out this way | `docs/ARCHITECTURE.md` |
| Find the actual blueprints | `blueprints/` |

Everything else supports one of those five things.

## Files GitHub reads specially

A few files aren't just for people, GitHub itself reads them and changes how the website
behaves. That's why they need to be in exact spots with exact names.

| File | What it does |
| --- | --- |
| `README.md` | Shows automatically on the project's front page |
| `LICENSE` | Says who is allowed to use this code, and how |
| `CODE_OF_CONDUCT.md` | Adds a link to the community info on GitHub |
| `CONTRIBUTING.md` | GitHub links this when someone opens an issue or PR |
| `SECURITY.md` | Powers the Security tab's "Report a vulnerability" button |
| `.github/PULL_REQUEST_TEMPLATE.md` | Fills in the box when someone opens a pull request |
| `.github/ISSUE_TEMPLATE/*.yml` | Turns "New issue" into a set of forms |
| `.github/CODEOWNERS` | Automatically asks the right people to review a change |
| `.github/workflows/ci.yml` | Runs checks automatically on every push |
| `.gitignore` | Tells git which files to never save |

Move or rename one of these and the feature just quietly stops working, with no error
message. Good to know before you go rearranging things.

## The root folder

**`README.md`**, the front page. What the project is, why it exists, how to get started.

**`LICENSE`**, ours is MIT. It means anyone can use, copy, or build on this code, including
for commercial projects. Without this file, nobody is legally allowed to reuse the code at
all, even though it's public.

**`CONTRIBUTING.md`**, the whole process for contributing, in one short page.

**`CODE_OF_CONDUCT.md`**, how we treat each other, and what happens if someone doesn't.

**`AI_POLICY.md`**, our own addition. AI tools are fine, submitting code you can't explain is
not.

**`SECURITY.md`**, how to report a security problem privately, rather than in a public issue.

**`MAINTAINERS.md`**, who's running the project and how to reach them.

**`.gitignore`**, a list of files git should ignore, things like `.env` files and cache
folders. Without it, those would get accidentally uploaded and clutter every change.

## `.github/`

Settings for GitHub itself.

**`workflows/ci.yml`**, runs a check automatically every time someone pushes code: does
every blueprint's `blueprint.yaml` look right, do the required files exist. Green tick means
good, red cross means something needs fixing. This means a reviewer doesn't have to manually
check any of that themselves.

**`PULL_REQUEST_TEMPLATE.md`**, the checklist that appears when opening a pull request.

**`ISSUE_TEMPLATE/`**, turns "New issue" into a few simple forms, one for proposing a
blueprint, one for bugs.

**`CODEOWNERS`**, when someone changes certain files, it automatically tags the right people
to review it. See [Adding maintainers](#adding-maintainers) below for how to set this up.

**`dependabot.yml`**, opens a pull request automatically when a dependency has a newer
version.

## `docs/`

Our own standards, written for contributors.

| File | For |
| --- | --- |
| `ARCHITECTURE.md` | Why the blueprints folder is laid out this way |
| `blueprint-guide.md` | The exact steps and shape a new blueprint should follow |
| `standards.md` | How to write good code and configuration here |

## `blueprints/`

The actual blueprints, once they exist. Grouped into `backend/`, `frontend/`, and
`fullstack/`. Right now these are empty, that's expected, not broken, we're setting up the
foundation first.

`blueprints/README.md` is the running list of every blueprint and how finished each one is.

## `template/`

The blank starting point copied when someone begins a new blueprint. Nobody edits this
directly, `tools/new_blueprint.py` copies it.


## Glossary

**Repository (repo)**, the whole project folder, with its full history of changes.

**Git vs GitHub**, git is the tool that tracks changes on your computer. GitHub is the
website that hosts the project online and adds things like issues and pull requests. Git
works fine without any internet connection.

**Commit**, a saved snapshot of some changes, with a short message describing them.

**Branch**, a separate line of work, so you can make changes without touching the main
version until you're ready. `main` is the primary branch.

**Push / pull**, uploading your commits to GitHub, or downloading someone else's.

**Fork**, your own personal copy of someone else's project on GitHub. How outside
contributors work on a project they can't directly edit.

**Pull request (PR)**, "please add my changes to your project." This is where review and
discussion happen before something gets merged in.

**Merge**, accepting a pull request's changes into `main`.

**Issue**, a tracked task, bug, or question. Most work starts as an issue.

**CI**, short for Continuous Integration, the automatic checks that run on every push.

**Maintainer**, someone who can approve and merge pull requests, and looks after part of the
project.

**Steward**, the person looking after one specific blueprint day to day.
