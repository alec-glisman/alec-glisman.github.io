# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Academic personal website for Alec Glisman, built with Jekyll on the Academic Pages template (fork of Minimal Mistakes). Hosted on GitHub Pages at https://alec-glisman.github.io/.

## Build & Development Commands

```bash
# Install dependencies
bundle install

# Local development with live reload
bundle exec jekyll liveserve

# Build static site
bundle exec jekyll build

# Minify JavaScript assets
npm run build:js

# Watch JS for changes during development
npm run watch:js
```

Development server runs at `http://localhost:4000`. Use `_config.dev.yml` for local overrides (expanded SCSS, no analytics).

GitHub Pages automatically builds and deploys on push to `main`.

## Architecture

- **Jekyll static site** using Liquid templates, Markdown content, and SCSS styling
- **_config.yml**: Main site configuration (author info, social links, collections, plugins)
- **_pages/**: Core site pages (about, publications, research, talks, teaching)
- **_publications/**, **_talks/**, **_teaching/**: Content collections rendered via Jekyll collections
- **_layouts/**: Page templates; **_includes/**: Reusable partial components
- **_sass/**: SCSS organized by component (inherits from Minimal Mistakes theme)
- **assets/js/**: Vendor and custom JS, minified via uglify-js
- **files/**: Downloadable documents (PDFs)
- **images/**: Site image assets

## Key Details

- Markdown engine: kramdown with GFM
- Syntax highlighting: Rouge
- Plugins: jekyll-paginate, jekyll-sitemap, jekyll-gist, jekyll-feed, jekyll-redirect-from
- No CI/CD pipelines — relies entirely on GitHub Pages built-in Jekyll compilation
- VS Code workspace includes cSpell dictionary for academic/research terminology

## Additional Configuration

@CLAUDE.scientific-writer.md
