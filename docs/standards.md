# How to build a good blueprint

This is the engineering bar for blueprints here. It is also, honestly, just a list of things
that make any project nicer to work on. If you apply half of it to your own side projects
you will already be ahead.

Read it once now, then come back to it while you build. You do not need to memorise it.

**You don't need all of this from day one.** Start messy, land something small, improve it as
you go. See [blueprint-guide.md](blueprint-guide.md) for the steps in order.

---

## Follow your framework's conventions first

A Django blueprint should look like a Django project. An Express blueprint should look like an
Express project. Do not invent a layout to make blueprints here look similar to each other.

Everything below describes *what* good looks like. *How* you get there is whatever is normal
in that ecosystem. If a rule here fights your framework's convention, follow the convention
and mention it in `ARCHITECTURE.md`.

---

## Project structure

**Keep application code in one obvious folder.** `src/`, `app/`, or whatever your framework
uses. Tests, config, and Docker files live outside it.

**Do not build a deep folder tree on day one.** Four files beat six folders with one file
each. Grow the structure when you have something to put in it.

**Keep business logic out of route handlers.** This is the one structural rule worth caring
about, because it is what makes code testable.

```python
# Harder to test: you can only reach this logic through an HTTP request
@router.post("/tasks")
def create_task(payload: TaskIn, db: Session = Depends(get_db)):
    if db.query(Task).filter_by(title=payload.title).first():
        raise HTTPException(409, "duplicate")
    task = Task(**payload.dict())
    db.add(task); db.commit()
    return task

# Easier to test: create_task() is a plain function you can call directly
@router.post("/tasks", status_code=201)
def create_task(payload: TaskIn, service: TaskService = Depends(get_task_service)):
    return service.create(payload)
```

**Avoid a `utils` file.** It is where code goes when nobody decided where it belongs, and it
grows forever. Name files for what they hold: `dates.py`, `pagination.py`.

---

## Configuration

**Read settings from environment variables, in one file only.** One `config.py` or
`config.ts` reads everything and exports a settings object. Everywhere else imports from it.

```python
# app/config.py, the only place os.environ appears
class Settings(BaseSettings):
    database_url: str
    log_level: str = "INFO"
    debug: bool = False

settings = Settings()
```

With one file you can see every setting the app has by opening one file. With `os.environ`
scattered around, nobody ever knows the full list.

**Crash at startup if something required is missing.** Print all the problems at once, then
exit:

```
Configuration error:
  DATABASE_URL: missing
  PORT: "eight thousand" is not a number
Copy .env.example to .env and fill it in.
```

This is the highest value thing in this whole document. The alternative is an app that starts
fine and then throws a confusing `NoneType` error deep inside a request at the worst possible
moment.

**Ship a `.env.example` with fake values only.** Every setting listed, each with a short
comment. For secrets, give a command to generate one rather than a value:

```bash
# Generate your own: python -c "import secrets; print(secrets.token_urlsafe(32))"
SECRET_KEY=replace-me
```

Never a realistic looking fake, because people paste those into production.

**Never commit `.env`.** If you do it by accident, tell a maintainer and change the password
or key straight away. Deleting the line in a later commit does not remove it from git history.

---

## Errors

**Catch everything in one place.** Most frameworks call this error middleware or an exception
handler. Without it, an unexpected error either crashes your app or dumps a stack trace to
whoever is using it.

**Use one shape for every error response**, so anyone calling your API can write one error
handler:

```json
{
  "error": {
    "code": "task_not_found",
    "message": "No task exists with id 42.",
    "request_id": "01J8XZ4K9P2M"
  }
}
```

**Never send stack traces, SQL, or file paths to users.** Those go in the logs. The user gets
a plain message plus the `request_id`, which is how you find the matching log entry.

**Use the right status code.** The two common mistakes: returning `200` with
`{"success": false}` (breaks every HTTP client in the chain), and returning `500` for what is
really the caller's mistake (buries your real bugs in noise).

| Code | Means |
| --- | --- |
| 400 | The request is malformed |
| 401 | We do not know who you are |
| 403 | We know who you are, and you may not |
| 404 | It does not exist |
| 409 | Conflicts with what is already there |
| 422 | Well formed, but the values are invalid |
| 500 | We broke |

**Validate input at the edge** with your framework's schema tool (Pydantic, Zod, serializers).
Return all the field errors at once, not one at a time, or the user needs five attempts to
submit a form.

**Never write `except: pass`.** If an error really is safe to ignore, log it and write a
comment saying why. Silent catches are where bugs hide for months.

---

## Logging

**Use a logging library, not `print`.** You cannot filter, route, or switch off `print`.

**Log fields, not sentences.**

```python
# Fine while debugging, useless later
print(f"User {user.id} created task {task.id}")

# Searchable, filterable, countable
logger.info("task.created", extra={"user_id": user.id, "task_id": task.id})
```

**Give every request an ID and put it in every log line for that request.** This is what turns
a jumble of interleaved lines into a readable story, and it is the single most useful logging
habit there is. Return the same ID to the client so a bug report points at the right logs.

**Write to the console, not to a file.** Docker and every hosting platform collect console
output automatically. An app that manages its own log files will quietly fill up a disk.

**Never log passwords, tokens, or whole request bodies.** The whole-body case is the sneaky
one: it looks harmless until someone adds a password field. Log IDs, not objects.

---

## Testing

**Get the test setup working even before you have much to test.** Wiring up a test database
and a client fixture from scratch is exactly the friction that stops people testing at all.
Do it once here and the fourth test becomes trivial.

**`make test` must work from a fresh clone** with no manual database setup.

**Tests must pass offline, in any order.** No network calls, no shared state between tests, no
`sleep`, no assertions on the current time.

**A flaky test is worse than no test.** It teaches everyone to re-run CI until it goes green,
and then a real failure gets re-run too. Fix it or delete it.

**Test the failure paths.** Happy path tests are the easy half. What happens with missing
config, a bad ID, an empty list, someone else's data? That is where the bugs live.

**Name tests so a failure explains itself:**

```python
def test_create_task_returns_409_when_title_already_exists(): ...
```

At 1am you want the test name to tell you what broke without opening the file.

**Do not chase a coverage percentage.** 95% coverage of happy paths is weaker than 60% that
covers the error branches.

---

## Docker

**Two commands should get someone running:**

```bash
cp .env.example .env
make docker-up
```

**Pin your base image.** `python:3.12-slim`, never `python:latest`. Otherwise your build
changes underneath you.

**Install dependencies before copying source**, or every one-line edit reinstalls everything:

```dockerfile
COPY requirements.txt .          # rarely changes, stays cached
RUN pip install -r requirements.txt
COPY . .                         # changes constantly
```

**Run as a non-root user.** One `USER` line.

**Add a `.dockerignore`** covering at least `.git`, `.env`, and `node_modules`. Without it
your build is slow and a stray `.env` can end up inside the image.

**Namespace everything in `docker-compose.yml` with your blueprint's name.** Project name,
container names, volumes, networks. Two blueprints that both call a volume `pgdata` will share
it, and the resulting mess is genuinely hard to diagnose:

```yaml
name: fastapi-rest
volumes:
  fastapi-rest-pgdata:      # not "pgdata"
```

**Bind databases to localhost only:** `"127.0.0.1:8011:5432"`, not `"8011:5432"`. The second
form puts your dev database on the Wi-Fi network.

**Use `condition: service_healthy` in `depends_on`.** A plain `depends_on` waits for the
container to *start*, not to be *ready*, which is the most common cause of "works on my
machine, fails in CI".

---

## Formatting and linting

**Use your ecosystem's standard tools with default settings.** Ruff or Black for Python,
Prettier or Biome for JavaScript, `gofmt` for Go. Do not spend an evening tuning line length.

**Commit the config file** inside your blueprint, so CI and your laptop run identical rules.

**Zero warnings.** Not "no errors, some warnings". A codebase with 40 tolerated warnings has
40 things nobody reads, and number 41 is the real bug.

If a rule genuinely does not fit, switch it off in the config file with a comment saying why.
A bare `# noqa` with no explanation will get a comment in review.

---

## Documentation

**Your README's Getting Started section must work exactly as written**, from a fresh clone,
with nothing else installed. Test it by actually doing it. This is the most common reason a
blueprint fails review.

**Be honest about what is missing.** A "What's Included" section with a ✅ list and a ❌ list
is the thing that makes people trust the repo:

```markdown
- ✅ Structured logging with request IDs
- ✅ Docker, non-root, with a health check
- ❌ No authentication
- ❌ No rate limiting
```

**`ARCHITECTURE.md` explains why, not how.** The most useful thing you can write is the option
you *rejected* and the reason. The code shows what you chose; nothing shows what you did not.

**Comments explain why, not what.**

```python
# Bad: says what the code already says
counter += 1  # increment counter

# Good: says something the code cannot
# Advisory lock rather than SELECT FOR UPDATE: the row may not exist yet.
```

**No commented-out code, no bare `TODO`s.** Delete it, it is in git history. A TODO with no
issue attached is a wish.

---

## Security basics

Most of this you get for free by following the sections above. The rest:

**Never commit secrets.** Public repos are scanned by bots continuously. A key committed and
removed ten minutes later has already been taken.

**Never build queries by joining strings.** Use parameters or your ORM. Same for shell
commands and file paths.

```python
db.execute(f"SELECT * FROM users WHERE email = '{email}'")            # SQL injection
db.execute("SELECT * FROM users WHERE email = :email", {"email": email})   # fine
```

**Pin your dependencies and commit the lockfile.**

**Do not use `Access-Control-Allow-Origin: *` with credentials.** List your allowed origins in
config.

---

## Authentication

**Authentication is optional.** A blueprint without it is not incomplete, it is a blueprint
without auth, and its manifest says so.

If you do add it, this section is not advice, it is a requirement, and the review is stricter
than anywhere else. People copy auth code into real projects and then stop thinking about it.
A subtle bug here does not hurt this repo, it hurts everyone who built on it.

**Extra rules for auth pull requests:** two reviewers, and the tests listed below.

**Pick the simplest thing that fits:**

1. **An existing provider** (OAuth, or a hosted auth service). You handle no passwords at all.
   Best option when it fits.
2. **Server-side sessions with a cookie.** The default for anything a browser talks to.
   Boring, well understood, and you can log someone out by deleting a row.
3. **JWTs.** Right for service-to-service. Usually wrong for browser apps, whatever tutorials
   say, because you cannot revoke them and there is no clean place to store them.

**Never invent your own.** No custom token formats, no hand-rolled crypto.

**The rules:**

- Hash passwords with **Argon2id**, bcrypt, or scrypt. Never SHA-256 or MD5: they are fast,
  which is exactly wrong here. The library handles salting.
- Minimum 12 characters. **No composition rules**, they just produce `Password1!`.
- Wrong password and unknown user must return the **same message and take the same time**.
  Otherwise your login page tells attackers who has an account.
- **Rate limit** login and registration, by IP and by account. Without this any password
  policy is decorative.
- Cookies get `HttpOnly`, `Secure`, `SameSite=Lax`, and an expiry. Rotate the session ID on
  login, and destroy it server-side on logout.
- **Never put tokens in `localStorage`.** Any XSS bug reads it instantly.
- **Filter by owner inside the query**, not after fetching:

```python
# Wrong: fetches someone else's row first
task = db.get(Task, task_id)
if task.owner_id != user.id: raise Forbidden()

# Right: the query cannot return it
task = db.query(Task).filter_by(id=task_id, owner_id=user.id).one_or_none()
```

**Tests you must have if you have auth:**

- [ ] Stored password is hashed, not plaintext
- [ ] Login works with the right password
- [ ] Wrong password and unknown user give identical responses
- [ ] A protected route without a token returns 401
- [ ] A protected route with a tampered or expired token returns 401
- [ ] Reading another user's record returns 404 and never their data
- [ ] Logout actually invalidates the session server-side
- [ ] Rate limiting kicks in after N failed attempts
- [ ] Passwords never appear in logs or error responses
