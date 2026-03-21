# Setup Guide: Building and Testing the Site

This guide covers how to set up the development environment for building and testing the Jekyll site.

## Prerequisites

- **Ruby 3.0+** (system Ruby 2.6 is too old for `github-pages` gem)
- **Bundler** (gem dependency manager)
- **Python 3.9+** (for test suite)
- **Node.js** (optional, only needed for JS minification - currently not in use)

## Option A: Using rbenv (Recommended)

If you have [rbenv](https://github.com/rbenv/rbenv) installed:

```bash
# Install Ruby 3.3.10 (or any version >= 3.0)
rbenv install 3.3.10

# Set local Ruby version for this project
echo "3.3.10" > .ruby-version

# Install Bundler and gems
bundle install

# Build the site
bundle exec jekyll build

# Run with live reload (port 4000)
bundle exec jekyll liveserve
```

## Option B: Using Homebrew

If you prefer to install Ruby globally via Homebrew:

```bash
# Install latest Ruby
brew install ruby

# Update PATH to use Homebrew ruby (add to ~/.zshrc or ~/.bash_profile)
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"

# Verify Ruby version
ruby --version  # Should be 3.0 or higher

# Install Bundler
gem install bundler

# Install site dependencies
bundle install

# Build
bundle exec jekyll build
```

## Option C: Using Docker (Advanced)

If you have Docker installed:

```dockerfile
FROM ruby:3.3-slim
WORKDIR /site
COPY Gemfile Gemfile.lock ./
RUN bundle install
COPY . .
RUN bundle exec jekyll build
EXPOSE 4000
CMD ["bundle", "exec", "jekyll", "liveserve", "--host", "0.0.0.0"]
```

Build and run:
```bash
docker build -t site .
docker run -it -p 4000:4000 -v $(pwd):/site site
# Visit http://localhost:4000
```

## Setting Up the Test Suite

After installing Ruby and building the site:

```bash
# 1. Create Python virtual environment
python3 -m venv venv

# 2. Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows

# 3. Install test dependencies
cd tests
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install chromium

# 5. Run tests
pytest              # All tests
pytest unit/        # Unit tests only (fast)
pytest -v -m unit   # Verbose unit tests
```

## Running Tests

### All Tests
```bash
cd tests
source ../venv/bin/activate  # Activate venv
make test           # All tests
```

### Fast Unit Tests Only (5-10 seconds)
```bash
make test-unit
```

### Integration Tests (requires HTTP server, 10-15 seconds)
```bash
make test-integration
```

### Full Test Suite
```bash
make test           # All categories (2-3 minutes total)
```

### Generate Test Report
```bash
pytest --html=report.html --self-contained-html
```

## Troubleshooting

### "You don't have write permissions for the /Library/Ruby/Gems/"

This means you're trying to use the system Ruby with `sudo gem install`. Don't use `sudo`. Instead, use rbenv or Homebrew Ruby installation.

### "Ruby version >= 3.0 required"

The `github-pages` gem only works with Ruby 3.0 or newer. Install a newer Ruby:

```bash
# Using rbenv
rbenv install 3.3.10
echo "3.3.10" > .ruby-version

# Using Homebrew
brew install ruby  # Will install latest
```

### "Could not find 'bundler' (X.X.X)"

Remove the old Gemfile.lock and regenerate it:

```bash
rm Gemfile.lock
bundle install
```

### Playwright Installation Fails

If `playwright install chromium` fails, try:

```bash
pip install --upgrade playwright
python -m playwright install chromium
```

### Jekyll Build Hangs

If `bundle exec jekyll build` hangs, interrupt it (Ctrl+C) and try with verbose output:

```bash
bundle exec jekyll build --verbose
```

## Verifying Installation

```bash
# Check Ruby version
ruby --version         # Should be >= 3.0.0

# Check Bundle is installed
bundle --version      # Should be version

# Test site build
bundle exec jekyll build
# Should create _site/ directory

# Check Python test suite
source venv/bin/activate
pytest --version       # Should show pytest version
pytest unit/test_build.py::TestBuildProcess::test_site_builds_without_errors -v
# Should PASS if _site/ exists
```

## Development Workflow

```bash
# 1. Start with venv activated
source venv/bin/activate

# 2. Make changes to site source files

# 3. Rebuild if needed
bundle exec jekyll build

# 4. Or use live reload
bundle exec jekyll liveserve
# Visit http://localhost:4000

# 5. Run tests to verify
cd tests && make test-unit
```

## Quick Commands

```bash
# Build site
bundle exec jekyll build

# Serve with live reload
bundle exec jekyll liveserve

# Run unit tests only
source venv/bin/activate && cd tests && make test-unit

# Run all tests
source venv/bin/activate && cd tests && make test

# Clean test cache
cd tests && make clean
```

## Next Steps

1. Install Ruby 3.0+ using rbenv or Homebrew
2. Run `bundle install` to install gem dependencies
3. Run `bundle exec jekyll build` to build the site
4. Follow "Setting Up the Test Suite" above
5. Run `cd tests && make test-unit` to verify

For more details on the test suite, see [`tests/README.md`](tests/README.md).
