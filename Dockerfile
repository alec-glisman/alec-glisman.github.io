# ──────────────────────────────────────────────
# Stage 1: base — Ruby gems shared by all stages
# ──────────────────────────────────────────────
FROM ruby:3.3-slim AS base

# System deps needed to compile native gems (nokogiri, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /site

COPY Gemfile* ./
RUN bundle install --jobs 4 --retry 3 \
    # Jekyll 3.10.0 bug: @mime_types_charset can be nil for some MIME types.
    # Add safe-navigation (&.) so the servlet doesn't crash on every GET request.
    # Upstream fix: https://github.com/jekyll/jekyll/issues/9526
    && SERVLET=$(bundle show jekyll)/lib/jekyll/commands/serve/servlet.rb \
    && sed -i 's/return unless @mime_types_charset\.key?/return unless @mime_types_charset\&.key?/' "$SERVLET" \
    # Ruby 3.2+ removed String#tainted? but Liquid 4.0.3 still calls it.
    # Monkey-patch the missing method so Jekyll builds succeed.
    && LIQUID_VAR=$(bundle show liquid)/lib/liquid/variable.rb \
    && sed -i 's/return unless obj\.tainted?/return unless obj.respond_to?(:tainted?) \&\& obj.tainted?/' "$LIQUID_VAR" \
    # pathutil 0.16.2 passes keyword args as a positional Hash to File.read/binread/readlines.
    # Ruby 3.x requires **kwd (double-splat) to forward keyword arguments correctly.
    && PATHUTIL=$(bundle show pathutil)/lib/pathutil.rb \
    && sed -i 's/self, \*args, kwd/self, *args, **kwd/g' "$PATHUTIL"

# ──────────────────────────────────────────────
# Stage 2: dev — local development with live reload
# ──────────────────────────────────────────────
FROM base AS dev

COPY . .

EXPOSE 4000 35729

# Live-reload server bound to 0.0.0.0 so Docker port mapping works
CMD ["bundle", "exec", "jekyll", "liveserve", "--host", "0.0.0.0", "--livereload-port", "35729"]

# ──────────────────────────────────────────────
# Stage 3: build — produce the static _site/
# ──────────────────────────────────────────────
FROM base AS build

COPY . .
RUN bundle exec jekyll build

# ──────────────────────────────────────────────
# Stage 4: test — Python + Playwright + built site
# ──────────────────────────────────────────────
FROM python:3.12-slim AS test

# Ruby runtime (needed for Jekyll build inside tests/conftest.py)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ruby \
    ruby-dev \
    build-essential \
    git \
    # Playwright Chromium system dependencies
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpango-1.0-0 \
    libcairo2 \
    && rm -rf /var/lib/apt/lists/*

# Upgrade RubyGems so it can resolve Bundler 4.x, then install the locked version
RUN gem update --system --no-document \
    && gem install bundler --no-document

WORKDIR /site

# Install Ruby gems
COPY Gemfile* ./
RUN bundle install --jobs 4 --retry 3 \
    # Jekyll 3.10.0 bug: @mime_types_charset can be nil for some MIME types.
    && SERVLET=$(bundle show jekyll)/lib/jekyll/commands/serve/servlet.rb \
    && sed -i 's/return unless @mime_types_charset\.key?/return unless @mime_types_charset\&.key?/' "$SERVLET" \
    # Ruby 3.2+ removed String#tainted? but Liquid 4.0.3 still calls it.
    # Monkey-patch the missing method so Jekyll builds succeed.
    && LIQUID_VAR=$(bundle show liquid)/lib/liquid/variable.rb \
    && sed -i 's/return unless obj\.tainted?/return unless obj.respond_to?(:tainted?) \&\& obj.tainted?/' "$LIQUID_VAR" \
    # pathutil 0.16.2 passes keyword args as a positional Hash to File.read/binread/readlines.
    # Ruby 3.x requires **kwd (double-splat) to forward keyword arguments correctly.
    && PATHUTIL=$(bundle show pathutil)/lib/pathutil.rb \
    && sed -i 's/self, \*args, kwd/self, *args, **kwd/g' "$PATHUTIL"

# Install Python dependencies and Playwright browser
COPY tests/requirements.txt tests/requirements.txt
RUN pip install --no-cache-dir -r tests/requirements.txt \
    && playwright install chromium \
    && playwright install-deps chromium

# Copy full source
COPY . .

WORKDIR /site/tests

CMD ["make", "test"]
