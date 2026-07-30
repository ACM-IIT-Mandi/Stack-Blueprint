# Security Policy

This repo does not run any live service of its own, but the code in it is meant to be copied
into other people's real projects. So a security bug in a blueprint matters, even though
nothing here is actually deployed anywhere.

## What counts as a security issue

Things like:

- A way to log in as someone else, or bypass authentication
- SQL injection, command injection, or similar
- A real secret or credential accidentally committed
- A container running as root when it should not
- Something in our GitHub Actions setup that could leak secrets

Not security issues (open a normal bug report instead):

- A blueprint simply not having a feature yet (no auth, no rate limiting). That is a gap, not
  a vulnerability, and the README says so honestly.

## How to report

**Do not open a public issue for this.** Instead, use GitHub's private reporting: go to the
**Security** tab of this repo, then **Report a vulnerability**.

If that is not available for some reason, message a maintainer directly (see
[MAINTAINERS.md](MAINTAINERS.md)).

Please include what is affected, how to reproduce it, and what someone could do with it. You
do not need a working exploit, a clear explanation is enough.

## What happens after

We are students maintaining this alongside classes, so please be patient, but we will aim to:

- Reply within about a week
- Confirm or explain within two weeks
- Agree a fix and a timeline with you before anything is made public

## If you accidentally commit a secret

Do not just delete it in the next commit, since it stays in the git history either way.
Instead, change the password or regenerate the key straight away, then let a maintainer
know so we can clean up the history if needed.
