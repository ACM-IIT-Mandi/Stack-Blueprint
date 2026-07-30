<!--
Thanks for contributing.

Feel free to open this as a draft early if you want feedback partway through.
-->

## What this changes

<!-- One or two sentences. -->

Closes #

## Type

- [ ] New blueprint (link the approved proposal issue)
- [ ] New feature or improvement in an existing blueprint
- [ ] Bug fix
- [ ] Documentation
- [ ] Something else in the project setup

---

## Explain what you did

**A couple of sentences, in your own words, not copied from anywhere.**

1. **What does this do, and why does it work?**

   <!-- Your answer -->

2. **What's one decision you made, and why did you make it that way?**

   <!-- e.g. "I used server-side sessions instead of JWTs because the client is always a
        browser and revoking a session on logout matters more here." -->

<!--
This is the most useful thing a reviewer reads. If it's hard to write, that usually means
there's a part you haven't fully understood yet, which is worth knowing now rather than
later. See AI_POLICY.md.
-->

---

## Checklist

- [ ] `make check` passes
- [ ] I ran this from a genuinely fresh clone, following the README as written
- [ ] `blueprint.yaml`'s `features` list matches what actually works
- [ ] No `.env` file or real secrets committed

**If this adds a new blueprint:**

- [ ] Follows the layout in [docs/blueprint-guide.md](../docs/blueprint-guide.md)
- [ ] Row added or updated in [blueprints/README.md](../blueprints/README.md)

**If this adds or changes authentication:**

- [ ] A second reviewer is tagged
- [ ] Every test listed in the authentication section of [docs/standards.md](../docs/standards.md) exists and passes

---

## AI use

- [ ] I used an AI tool for part of this

No downside to ticking this, see [AI_POLICY.md](../AI_POLICY.md). What matters is that you
can explain what you submitted if asked.

## Anything else

<!-- Questions, things you're unsure about, parts you'd like a closer look at.
     "I'm not confident about the error handling here" is genuinely useful to say. -->
