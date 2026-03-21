# Alec Glisman's Academic Website

My professional website built with Jekyll on the Academic Pages template. Hosted on GitHub Pages at **[alec-glisman.github.io](https://alec-glisman.github.io)**.

## Quick Start

### Prerequisites

- **Ruby 3.0+** (required for `github-pages` gem)
- **Bundler** (Ruby gem manager)
- **Python 3.9+** (for test suite)

### Run Locally

```bash
# Install Ruby dependencies
bundle install

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Install test dependencies
pip install -r tests/requirements.txt
playwright install chromium

# Start development server with live reload
bundle exec jekyll liveserve

# Visit http://localhost:4000
```

## Repository Structure

### Site Source Files

```
├── _config.yml                  # Main Jekyll configuration
├── _config.dev.yml              # Development overrides (expanded SCSS, no analytics)
│
├── _pages/                      # Core pages
│   ├── about.md                # Profile
│   ├── research.md             # Research overview
│   ├── experience.md           # Work experience
│   ├── projects.md             # Featured projects
│   ├── skills.md               # Technical skills
│   ├── publications.md         # Publication archive (auto-generated)
│   ├── talks.html              # Talks collection
│   ├── teaching.html           # Teaching collection
│   └── 404.md
│
├── _publications/               # Publication collection (5 entries)
│   ├── 2022-potential-flow-2.md
│   ├── 2024-langmuir-adsorption-isotherm.md
│   ├── 2024-macromolecules-polyelectrolyte.md
│   └── 2025-langmuir-binding-modes.md
│
├── _teaching/                   # Teaching collection
│   └── 2021-spring-ChE151b.md
│
├── _layouts/                    # Page templates
│   ├── default.html            # Base layout
│   ├── single.html             # Single page layout
│   └── archive.html            # Collection archive layout
│
├── _includes/                   # Reusable partials
│   ├── head/                   # Head components
│   ├── footer.html
│   ├── masthead.html
│   ├── navigation.html
│   └── scripts.html
│
├── _sass/                       # SCSS source files
│   ├── _variables.scss         # Colors, fonts, spacing
│   │                           # Navy #1B2A4A, Teal #0EA5C9, Inter font
│   ├── _custom.scss            # Custom design system
│   │                           # Animations, cards, buttons
│   └── [theme partials]        # Minimal Mistakes theme
│
├── _data/                       # YAML data files
│   ├── navigation.yml          # Main navigation menu
│   ├── authors.yml             # Author profile
│   └── ui-text.yml             # Localization strings
│
├── assets/
│   ├── css/main.scss           # Primary stylesheet
│   ├── js/main.min.js          # Minified JS bundle
│   └── js/_main.js             # Custom JS (scroll-reveal)
│
├── images/                      # Site images
│   ├── profile.png
│   └── [publication figures]
│
├── files/                       # Downloadable PDFs
│   └── [publication PDFs]
│
├── tests/                       # Comprehensive test suite (18 tests, 5 categories)
│   ├── conftest.py            # Pytest fixtures
│   ├── requirements.txt        # Python dependencies
│   ├── Makefile               # Test commands
│   ├── unit/                  # Source validation
│   ├── integration/           # HTML parsing
│   ├── acceptance/            # HTTP & accessibility
│   ├── regression/            # Change detection
│   └── e2e/                   # Browser automation
│
├── Gemfile                      # Ruby dependencies
├── .ruby-version               # Ruby version (3.0+)
├── package.json                # Node.js (minimal)
│
└── CLAUDE.md                    # Project guidance
```

### Design System

- **Primary Color**: Navy (#1B2A4A)
- **Accent Color**: Teal (#0EA5C9)
- **Font**: Inter (Google Fonts)
- **Base Theme**: Minimal Mistakes (forked as Academic Pages)

## Development

### Build & Commands

```bash
# Install dependencies
bundle install

# Local development with live reload (recommended)
bundle exec jekyll liveserve

# Build static site
bundle exec jekyll build

# Minify JavaScript
npm run build:js

# Watch JS for changes
npm run watch:js
```

**Development server:** <http://localhost:4000>

**Development config:** Use `_config.dev.yml` for local overrides (expanded SCSS, no analytics)

### File Editing

- **Content**: Edit `.md` or `.html` files in `_pages/`, `_publications/`, etc.
- **Styling**: Modify `_sass/` files (imported in `assets/css/main.scss`)
- **Navigation**: Edit `_data/navigation.yml`
- **Author Info**: Edit `_data/authors.yml`
- **Layout**: Modify `_layouts/` and `_includes/` templates

Changes are reflected immediately in live reload mode.

## Testing

A comprehensive Python-based test suite with 18 test files across 5 categories.

### Quick Reference

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
cd tests && make test

# Run by category (fast to slow)
make test-unit           # ~5-10s — Source validation only
make test-integration    # ~10-15s — HTML parsing
make test-regression     # ~10-15s — Change detection
make test-acceptance     # ~30-40s — HTTP & accessibility
make test-e2e           # ~60-90s — Browser automation

# Run specific test
pytest unit/test_build.py -v

# Update regression snapshots
pytest regression/ --update-snapshots

# Clean cache
make clean
```

### Test Categories

| Category | Purpose | Duration | Files |
|----------|---------|----------|-------|
| **Unit** | Source file validation (Jekyll build, YAML, front matter) | ~5-10s | `unit/` |
| **Integration** | HTML structure and content verification | ~10-15s | `integration/` |
| **Acceptance** | HTTP server, page status, WCAG accessibility | ~30-40s | `acceptance/` |
| **Regression** | CSS classes, colors, structure snapshots | ~10-15s | `regression/` |
| **E2E** | Playwright browser automation, navigation, animations | ~60-90s | `e2e/` |

### Test Coverage

- ✅ Jekyll builds without errors
- ✅ All 5 publications build correctly
- ✅ YAML data files are valid
- ✅ HTML structure is correct (lang, title, nav, footer, meta tags)
- ✅ Internal links resolve to existing files
- ✅ All pages return HTTP 200
- ✅ WCAG accessibility compliance (axe-core)
- ✅ Custom CSS classes are present
- ✅ Design colors are applied
- ✅ Navigation works between pages
- ✅ Scroll-reveal animations trigger
- ✅ Responsive design (mobile, tablet, desktop)

See [`tests/README.md`](./tests/README.md) for detailed test documentation.

## Environment Setup

### Option A: Using rbenv (Recommended)

```bash
# Install Ruby 3.3.10
rbenv install 3.3.10

# Set local Ruby version
echo "3.3.10" > .ruby-version

# Install Bundler and gems
bundle install
```

### Option B: Using Homebrew

```bash
# Install Ruby
brew install ruby

# Update PATH (add to ~/.zshrc or ~/.bash_profile)
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"

# Install Bundler
gem install bundler

# Install gems
bundle install
```

### Option C: Using Docker

```bash
# Build and run
docker build -t site .
docker run -it -p 4000:4000 -v $(pwd):/site site

# Visit http://localhost:4000
```

See [`SETUP.md`](./SETUP.md) for detailed setup instructions.

## Deployment

**Automatic:** Push to `main` branch — GitHub Pages automatically builds and deploys.

**Build Process:**

1. GitHub Pages runs Jekyll build
2. Static files are generated to `_site/`
3. Site is deployed to `https://alec-glisman.github.io`

No CI/CD pipelines required — GitHub Pages handles everything.

## Configuration

### Jekyll Config (`_config.yml`)

- Site title, author, baseurl
- Collections: publications, talks, teaching
- Plugins: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed, jekyll-redirect-from
- Markdown: kramdown with GFM
- Syntax highlighting: Rouge

### Development Config (`_config.dev.yml`)

Local overrides for development:

- Expanded SCSS output (no minification)
- Analytics disabled

Use during development: `jekyll liveserve` automatically applies `_config.dev.yml`.

## Content Guidelines

For creating and maintaining content, see the [Scientific Writer Guidelines](./CLAUDE.scientific-writer.md) for best practices on:

- Tone and style
- Formatting and structure
- Proper citations
- Consistency across the site

## Troubleshooting

### Ruby/Bundler

**"Ruby version >= 3.0 required"**

```bash
rbenv install 3.3.10 && echo "3.3.10" > .ruby-version
```

**"Could not find bundler"**

```bash
rm Gemfile.lock && bundle install
```

### Python/Tests

**"playwright: browser not installed"**

```bash
python -m playwright install chromium
```

**"pytest: command not found"**

```bash
source venv/bin/activate  # Ensure venv is activated
pip install -r tests/requirements.txt
```

See [`SETUP.md`](./SETUP.md) for additional troubleshooting.

## Development Workflow

```bash
# 1. Install dependencies (one-time)
bundle install
python3 -m venv venv
source venv/bin/activate
pip install -r tests/requirements.txt

# 2. Start development server
bundle exec jekyll liveserve

# 3. Edit content in _pages/, _publications/, etc.

# 4. Run tests before committing
cd tests && make test-unit    # Fast
cd tests && make test         # Full suite

# 5. Commit and push to main
git add .
git commit -m "Your message"
git push origin main
```

## Performance

| Task | Duration |
|------|----------|
| Unit tests only | ~5-10s |
| Full test suite | ~2-3 min |
| Jekyll build | ~5-10s |
| Jekyll live reload | ~1-2s per change |

## Resources

- [Jekyll Documentation](https://jekyllrb.com/)
- [Academic Pages Theme](https://github.com/academicpages/academicpages.github.io)
- [Minimal Mistakes Theme](https://mmistakes.github.io/minimal-mistakes/)
- [pytest Documentation](https://docs.pytest.org/)
- [Playwright Python Docs](https://playwright.dev/python/)

## License

[Specify your license here if applicable]

## Contact

**Website:** <https://alec-glisman.github.io>

---

**Last Updated:** March 2026
