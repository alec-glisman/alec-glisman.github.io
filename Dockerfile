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

COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4 --retry 3

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

# Install bundler for the Ruby layer
RUN gem install bundler --no-document

WORKDIR /site

# Install Ruby gems
COPY Gemfile Gemfile.lock ./
RUN bundle install --jobs 4 --retry 3

# Install Python dependencies and Playwright browser
COPY tests/requirements.txt tests/requirements.txt
RUN pip install --no-cache-dir -r tests/requirements.txt \
    && playwright install chromium \
    && playwright install-deps chromium

# Copy full source
COPY . .

WORKDIR /site/tests

CMD ["make", "test"]
