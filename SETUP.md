# Setup Guide

## Prerequisites

- **Docker Desktop** — download from <https://www.docker.com/products/docker-desktop/> and start it.

---

## Development Server

```bash
docker compose up dev
```

Visit <http://localhost:4000>. The site auto-reloads when source files change (LiveReload on port 35729).

---

## Test Suite

```bash
# Full test suite
docker compose run test

# Specific test category
docker compose run test make test-unit
docker compose run test make test-integration
docker compose run test make test-acceptance
docker compose run test make test-regression
docker compose run test make test-e2e
```

---

## Docker Image Targets

| Target  | Purpose                                     |
|---------|---------------------------------------------|
| `dev`   | Live-reload development server (port 4000)  |
| `build` | One-shot static site compilation            |
| `test`  | Full test suite (Python + Playwright)       |

---

## Rebuilding after Gemfile changes

```bash
docker compose down -v   # Remove the bundle_cache volume
docker compose build
```

---

## Troubleshooting

**Port 4000 already in use**

```bash
lsof -i :4000
kill -9 <PID>
```

**Gem/bundle cache stale after Gemfile change**

```bash
docker compose down -v
docker compose build
```

**Jekyll build hangs**

```bash
docker compose run --rm dev bundle exec jekyll build --verbose
```

---

## Quick Reference

| Task               | Command                                                    |
|--------------------|------------------------------------------------------------|
| Start dev server   | `docker compose up dev`                                    |
| Build static site  | `docker compose run --rm build bundle exec jekyll build`  |
| Run all tests      | `docker compose run test`                                  |
| Run unit tests     | `docker compose run test make test-unit`                   |
| Clean test cache   | `docker compose run test make clean`                       |

For more details on the test suite, see [`tests/README.md`](tests/README.md).
