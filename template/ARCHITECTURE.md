<!-- The README explains HOW to run this. This file explains WHY it is built this way.
     Write it once things are working, it is much easier while the reasoning is fresh.
     Guidance: docs/standards.md -->

# Architecture

## Overview

TODO: a short paragraph or two. What are the main parts, and how do they fit together?

## Structure

TODO: what each folder is for, and which way things depend on each other.

```
TODO/
  routes/     HTTP handlers, thin, no business logic
  services/   business logic, does not know about HTTP
  models/     data layer
```

Routes depend on services, services depend on models, not the other way round. That way the
business logic can be tested directly, without going through an HTTP request.

## Adding a feature

TODO: pick a real example and list the exact files you would touch, in order. This is what
turns this file from something people read into something they can actually use.

## A couple of decisions worth explaining

<!-- Two is enough. The useful part is the option you did NOT pick, and why, since the code
     only shows what you did pick. -->

### TODO: decision title

What we did: TODO

What we considered instead: TODO

Why we went the other way: TODO

## Known limitations

TODO: anywhere this design falls short, said plainly. For example, "the rate limiter only
works with one instance running, move it to Redis before running more than one."
