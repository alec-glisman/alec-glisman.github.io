# Setup Guide: Building and Testing the Site

This guide covers how to set up the development environment for the Jekyll site.

## Prerequisites

- **Docker Desktop** (recommended — handles all Ruby/Python dependencies automatically)
- *Alternative*: Ruby 3.0+, Python 3.9+, Bundler (see native options below)

---

## Option A: Docker (Recommended)

No Ruby, Python, or system gem configuration required — Docker handles everything.

### 1. Install Docker Desktop

Download from <https://www.docker.com/products/docker-desktop/> and start it.

### 2. Start the development server

```bash
docker compose up dev
```

Visit <http://localhost:4000>. The site auto-reloads when source files change (LiveReload on port 35729).

### 3. Run the test suite

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

### 4. Build the static site only

```bash
docker compose build build
```

The compiled site lands in `_site/` inside the container. To extract it:

```bash
docker compose run --rm build sh -c "bundle exec jekyll build"
```

### Docker image targets

| Target  | Purpose                                     |
|---------|---------------------------------------------|
| `dev`   | Live-reload development server (port 4000)  |
| `build` | One-shot static site compilation            |
| `test`  | Full test suite (Python + Playwright)       |

### Rebuilding after Gemfile changes

```bash
docker compose build
```

---

## Option B: Native — rbenv (macOS/Linux)

```bash
# Install Ruby 3.3.10
rbenv install 3.3.10
echo "3.3.10" > .ruby-version

# Install gems
bundle install

# Build the site
bundle exec jekyll build

# Serve with live reload
bundle exec jekyll liveserve
```

### Test suite (native)

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies and Playwright browser
cd tests
pip install -r requirements.txt
playwright install chromium

# Run tests
make test        # All tests
make test-unit   # Fast unit tests only
```

---

## Option C: Native — Homebrew (macOS)

```bash
brew install ruby
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
gem install bundler
bundle install
bundle exec jekyll liveserve
```

---

## Verifying Installation

```bash
# Ruby + Jekyll
ruby --version            # >= 3.0.0
bundle exec jekyll build  # Creates _site/

# Python test suite (native only)
source venv/bin/activate
pytest --version
pytest unit/test_build.py::TestBuildProcess::test_site_builds_without_errors -v
```

---

## Troubleshooting

### Docker: port 4000 already in use

```bash
# Find and stop the conflicting process
lsof -i :4000
kill -9 <PID>
```

### Docker: gem/bundle cache stale after Gemfile change

```bash
docker compose down -v   # Remove the bundle_cache volume
docker compose build
```

### Native: "You don't have write permissions for /Library/Ruby/Gems/"

Use rbenv or Homebrew Ruby — never `sudo gem install`.

### Native: "Ruby version >= 3.0 required"

```bash
rbenv install 3.3.10 && echo "3.3.10" > .ruby-version
# or
brew install ruby
```

### Native: "Could not find 'bundler'"

```bash
rm Gemfile.lock && bundle install
```

### Native: Playwright install fails

```bash
pip install --upgrade playwright
python -m playwright install chromium
```

### Jekyll build hangs

```bash
bundle exec jekyll build --verbose
```

---

## Development Workflow

```bash
# Docker (recommended)
docker compose up dev        # Start server
docker compose run test make test-unit  # Quick tests

# Native
source venv/bin/activate
bundle exec jekyll liveserve # http://localhost:4000
cd tests && make test-unit   # Quick tests
cd tests && make test        # Full suite before committing
```

---

## Quick Reference

| Task                    | Docker                                         | Native                                      |
|-------------------------|------------------------------------------------|---------------------------------------------|
| Start dev server        | `docker compose up dev`                        | `bundle exec jekyll liveserve`              |
| Build static site       | `docker compose run --rm build bundle exec jekyll build` | `bundle exec jekyll build`       |
| Run all tests           | `docker compose run test`                      | `cd tests && make test`                     |
| Run unit tests          | `docker compose run test make test-unit`       | `cd tests && make test-unit`                |
| Clean test cache        | `docker compose run test make clean`           | `cd tests && make clean`                    |

For more details on the test suite, see [`tests/README.md`](tests/README.md).
