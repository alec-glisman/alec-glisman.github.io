# Test Suite for alec-glisman.github.io

A comprehensive Python-based test suite for the Jekyll academic website covering unit, integration, acceptance, regression, and end-to-end testing.

## Overview

**Five test categories:**

| Category | Tests | Purpose |
|----------|-------|---------|
| **Unit** | `unit/` | Source file validation: Jekyll build, YAML data, front matter |
| **Integration** | `integration/` | Built HTML parsing: structure, links, content presence |
| **Acceptance** | `acceptance/` | HTTP server: page accessibility, status codes, WCAG accessibility |
| **Regression** | `regression/` | Detect changes: CSS classes, colors, structure snapshots |
| **End-to-End** | `e2e/` | Playwright browser: navigation, animations, responsive design |

## Quick Start

### Installation

```bash
# Install Python dependencies
pip3 install -r tests/requirements.txt

# Install Playwright browsers
playwright install chromium

# Verify installation
cd tests && pytest --co -q
```

### Running Tests

```bash
# All tests
make test

# By category
make test-unit              # Fast (no build/server needed)
make test-integration       # Parse HTML
make test-acceptance        # HTTP server tests
make test-regression        # Snapshots and CSS
make test-e2e              # Playwright browser

# Specific test file
pytest unit/test_build.py -v

# Update snapshots (regression tests)
pytest regression/ --update-snapshots
```

## Test Details

### Unit Tests (`unit/`)

**Files:** `test_build.py`, `test_data_files.py`, `test_front_matter.py`

- ✅ Jekyll build succeeds with no errors
- ✅ `_site/` directory structure is correct
- ✅ All expected pages are built (about, research, publications, experience, projects, skills, talks, teaching)
- ✅ All 5 publications are built
- ✅ CSS and JavaScript assets are compiled
- ✅ YAML data files are valid
- ✅ Navigation has exactly 7 items with correct URLs
- ✅ Authors data is complete and correct
- ✅ Publication front matter is complete
- ✅ No duplicate publication permalinks or titles
- ✅ No copy-paste duplicate excerpts

**Run:** `make test-unit` (~5-10 seconds)

### Integration Tests (`integration/`)

**Files:** `test_html_structure.py`, `test_internal_links.py`, `test_content.py`

- ✅ All pages have proper HTML structure (`<html lang>`, `<title>`, `<nav>`, `<footer>`)
- ✅ All meta tags present (description, OG tags)
- ✅ Inter font is loaded from Google Fonts
- ✅ Navy (#1B2A4A) and Teal (#0EA5C9) colors are in CSS
- ✅ All internal links resolve to existing files
- ✅ Navigation links all work
- ✅ Publication links all work
- ✅ Expected content is on each page:
  - About page: "Alec Glisman", "Merck", "Caltech"
  - Publications: all 5 titles and venues
  - Experience: "Senior AI/ML Scientist", past employers
  - Projects: project names and technologies
  - Skills: major skill categories
  - Research: 3 research themes with publication links

**Run:** `make test-integration` (~10-15 seconds)

### Acceptance Tests (`acceptance/`)

**Files:** `test_pages.py`, `test_accessibility.py`

**HTTP Server Tests:**
- ✅ All navigation pages return HTTP 200 (/, /research/, /publications/, /experience/, /projects/, /skills/, /talks/, /teaching/)
- ✅ All 5 publication pages return HTTP 200
- ✅ 404 page is handled correctly
- ✅ Pages load in < 500ms (performance baseline)
- ✅ Content-Type headers are correct (text/html)
- ✅ Redirects work (/about/ → /, /about.html → /)

**Accessibility Tests (axe-core via Playwright):**
- ✅ No critical or serious WCAG violations
- ✅ Color contrast is sufficient
- ✅ Navigation is keyboard accessible
- ✅ Passes basic accessibility checks

**Run:** `make test-acceptance` (~30-40 seconds)

### Regression Tests (`regression/`)

**Files:** `test_css_classes.py`, `test_snapshots.py`

**CSS Class Detection:**
- ✅ Custom CSS classes present in HTML:
  - `.reveal` (scroll animations)
  - `.research-card` (research sections)
  - `.experience-entry` (experience timeline)
  - `.project-card` (project showcase)
  - `.skill-tag` (skill badges)
- ✅ Color system is applied (Navy, Teal)
- ✅ Inter font is loaded
- ✅ Masthead has custom styling

**Snapshot Tests:**
- ✅ Navigation structure unchanged
- ✅ Publication list unchanged
- ✅ On first run, creates `snapshots/navigation.json` and `snapshots/publications.json`
- ✅ On subsequent runs, detects any changes

**Run:** `make test-regression` (~10-15 seconds)

### End-to-End Tests (`e2e/`)

**Files:** `test_navigation.py`, `test_animations.py`, `test_responsive.py`

**Navigation:**
- ✅ Can navigate between all main pages
- ✅ Can navigate to individual publication pages
- ✅ All 5 publications have links
- ✅ Browser back button works

**Animations:**
- ✅ Scroll-reveal animations initialize correctly
- ✅ `.is-visible` class is added after scrolling
- ✅ Hover effects work (nav links, cards)
- ✅ JavaScript executes correctly

**Responsive Design:**
- ✅ Mobile (375×812): page renders, content readable
- ✅ Tablet (768×1024): page renders correctly
- ✅ Desktop (1280×800): full navigation visible
- ✅ Orientation changes handled correctly (landscape ↔ portrait)

**Run:** `make test-e2e` (~60-90 seconds)

## Architecture

### Fixtures (conftest.py)

All session-scoped fixtures run once per test session:

```python
site_dir          # Build Jekyll site, return _site/ path
http_server       # Serve _site/ on localhost, return base_url
browser           # Launch headless Chromium
page              # New browser page for each test
axe_js            # Download/cache axe-core for accessibility
```

### Directory Structure

```
tests/
├── conftest.py                    # Session fixtures (build, HTTP server, browser)
├── requirements.txt               # Python dependencies
├── pytest.ini                     # pytest configuration
├── Makefile                       # Convenience commands
├── fixtures/
│   └── axe.min.js                # Downloaded once (accessibility testing)
├── unit/                          # Source file validation
│   ├── test_build.py
│   ├── test_data_files.py
│   └── test_front_matter.py
├── integration/                   # HTML parsing and verification
│   ├── test_html_structure.py
│   ├── test_internal_links.py
│   └── test_content.py
├── acceptance/                    # HTTP server and accessibility
│   ├── test_pages.py
│   └── test_accessibility.py
├── regression/                    # Detect unintended changes
│   ├── test_css_classes.py
│   ├── test_snapshots.py
│   └── snapshots/                 # Golden files (auto-generated)
│       ├── navigation.json
│       └── publications.json
└── e2e/                          # Browser automation
    ├── test_navigation.py
    ├── test_animations.py
    └── test_responsive.py
```

## Usage Examples

### Run unit tests only (fastest)
```bash
make test-unit
```

### Run all tests with verbose output
```bash
pytest -v
```

### Run a specific test
```bash
pytest acceptance/test_pages.py::TestNavigationPageAccess::test_nav_page_returns_200 -v
```

### Run tests and stop at first failure
```bash
pytest -x
```

### Run tests matching a keyword
```bash
pytest -k "navigation" -v
```

### Generate test report
```bash
pytest --html=report.html --self-contained-html
```

### Update regression snapshots
```bash
pytest regression/ --update-snapshots
```

### Clean up cache and snapshots
```bash
make clean
```

## Dependencies

- **pytest** ≥ 8.0.0 — Test framework
- **beautifulsoup4** ≥ 4.12.0 — HTML parsing
- **lxml** ≥ 5.0.0 — HTML parser backend
- **requests** ≥ 2.31.0 — HTTP client
- **pyyaml** ≥ 6.0.0 — YAML parsing
- **playwright** ≥ 1.44.0 — Browser automation

All dependencies are specified in `requirements.txt` and pinned to known-good versions.

## Troubleshooting

### "bundle: command not found"
The tests run `bundle exec jekyll build`. Make sure you're in the project root and have run `bundle install`.

```bash
cd /path/to/alec-glisman.github.io
bundle install
```

### "playwright: browser not installed"
After installing playwright via pip, run:

```bash
playwright install chromium
```

### "ConnectionRefusedError: connection failed" (E2E tests)
The HTTP server fixture failed to start. Check that no other process is using the random port assigned. This rarely happens; retrying usually works.

### Tests pass locally but fail on different system
Ensure Python 3.9+ is installed and all dependencies are installed from `requirements.txt`. The tests are designed to be platform-agnostic.

## Performance

| Test Category | Duration | Notes |
|---------------|----------|-------|
| Unit | ~5-10s | No build, fastest category |
| Integration | ~10-15s | Parses HTML, no network |
| Acceptance | ~30-40s | HTTP server, network requests |
| Regression | ~10-15s | File comparisons, snapshots |
| E2E | ~60-90s | Playwright, slowest category |
| **All** | ~2-3 min | First run (builds site once) |

Times vary based on system. Subsequent runs of unit tests only take 5-10 seconds.

## Continuous Integration

These tests are designed for local development. To add CI/CD:

```bash
# GitHub Actions example
git add .github/workflows/test.yml
```

(CI/CD is not set up by default — tests run locally via `make test`)

## Contributing

When making changes to the site:

1. **Run unit tests** — verify source files are valid
   ```bash
   make test-unit
   ```

2. **Run integration tests** — verify HTML is correct
   ```bash
   make test-integration
   ```

3. **Run all tests before committing**
   ```bash
   make test
   ```

4. **If tests fail** — check error message and fix the issue (not the test)

5. **If adding new pages** — add assertions to integration tests to verify content

6. **If changing CSS classes** — update regression tests and snapshots

## References

- [pytest documentation](https://docs.pytest.org/)
- [Playwright Python docs](https://playwright.dev/python/)
- [BeautifulSoup docs](https://www.crummy.com/software/BeautifulSoup/)
- [axe-core accessibility](https://github.com/dequelabs/axe-core)

---

**Last Updated:** March 2026
**Author:** Claude Code
**Site:** https://alec-glisman.github.io
