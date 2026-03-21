"""
Pytest configuration and fixtures for Jekyll site test suite.

Session-scoped fixtures:
- site_dir: Builds the site with 'bundle exec jekyll build'
- http_server: Serves _site/ on localhost using Python's http.server
- browser: Launches headless Chromium via Playwright
- axe_js: Downloads and caches axe-core.min.js for accessibility testing
"""

import json
import os
import shutil
import subprocess
import threading
import time
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from typing import Generator, Iterator

import pytest


# ============================================================================
# Globals and Configuration
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
SITE_DIR_DEFAULT = PROJECT_ROOT / "_site"
FIXTURES_DIR = Path(__file__).parent / "fixtures"
AXECORE_URL = "https://cdnjs.cloudflare.com/ajax/libs/axe-core/4.9.0/axe.min.js"


# ============================================================================
# Fixtures: Build System
# ============================================================================


@pytest.fixture(scope="session")
def project_root() -> Path:
    """Return path to project root."""
    return PROJECT_ROOT


@pytest.fixture(scope="session")
def site_dir(tmp_path_factory) -> Path:
    """
    Build the Jekyll site using 'bundle exec jekyll build'.

    Returns the path to the generated _site/ directory.
    Falls back to PROJECT_ROOT/_site if it exists.
    Provides helpful error message if build fails due to Ruby/Bundler issues.
    """
    # First, check if _site already exists in the project root
    # (user may have built it manually)
    existing_site = PROJECT_ROOT / "_site"
    if existing_site.exists() and (existing_site / "index.html").exists():
        print(f"\n✓ Using existing _site directory: {existing_site}")
        return existing_site

    # Use a temporary directory to build to, so we don't pollute the repo
    temp_build_dir = tmp_path_factory.mktemp("jekyll_build")

    # Run bundle exec jekyll build
    cmd = [
        "bundle", "exec", "jekyll", "build",
        "--source", str(PROJECT_ROOT),
        "--destination", str(temp_build_dir / "_site"),
    ]

    result = subprocess.run(
        cmd,
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True,
    )

    # Check for build success
    if result.returncode != 0:
        # Check for common Ruby/Bundler issues
        error_msg = result.stderr.lower() + result.stdout.lower()

        if "ruby version" in error_msg or "requires ruby" in error_msg:
            pytest.skip(
                "Jekyll build requires Ruby 3.0+. "
                "To install: rbenv install 3.2.0 && rbenv local 3.2.0 && bundle install"
            )
        elif "bundler" in error_msg and "could not find" in error_msg:
            pytest.skip(
                "Bundler version mismatch. "
                "To fix: rm Gemfile.lock && bundle install"
            )
        else:
            pytest.fail(
                f"Jekyll build failed.\n"
                f"Command: {' '.join(cmd)}\n"
                f"Exit code: {result.returncode}\n"
                f"STDOUT:\n{result.stdout}\n"
                f"STDERR:\n{result.stderr}\n\n"
                f"Try: cd {PROJECT_ROOT} && bundle install && bundle exec jekyll build"
            )

    # Check for errors/warnings in output (but not ruby version errors)
    if ("Error:" in result.stderr or "error:" in result.stderr) and "ruby version" not in result.stderr.lower():
        pytest.fail(
            f"Jekyll build reported errors in STDERR:\n{result.stderr}"
        )

    site_path = temp_build_dir / "_site"
    if not site_path.exists():
        pytest.fail(f"Jekyll build did not create _site directory at {site_path}")

    print(f"\n✓ Jekyll build successful: {site_path}")
    return site_path


# ============================================================================
# Fixtures: HTTP Server
# ============================================================================


class SilentHTTPRequestHandler(SimpleHTTPRequestHandler):
    """HTTP request handler that suppresses default logging."""

    def log_message(self, format, *args):
        """Suppress HTTP server log messages."""
        pass


def _run_http_server(
    site_dir: Path, port: int, stop_event: threading.Event
) -> None:
    """
    Run HTTP server in a thread.

    Args:
        site_dir: Directory to serve
        port: Port to listen on
        stop_event: threading.Event to signal shutdown
    """
    os.chdir(site_dir)
    server = HTTPServer(("localhost", port), SilentHTTPRequestHandler)
    server.timeout = 1

    while not stop_event.is_set():
        server.handle_request()

    server.server_close()


@pytest.fixture(scope="session")
def http_server(site_dir: Path) -> Iterator[str]:
    """
    Start an HTTP server serving _site/ on localhost.

    Yields the base URL (e.g. "http://localhost:8765").
    Server is stopped after all tests.
    """
    # Find an available port (use 0 to let OS choose)
    import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("localhost", 0))
    port = sock.getsockname()[1]
    sock.close()

    # Start server in background thread
    stop_event = threading.Event()
    server_thread = threading.Thread(
        target=_run_http_server,
        args=(site_dir, port, stop_event),
        daemon=True,
    )
    server_thread.start()

    # Give server time to start
    time.sleep(0.5)

    base_url = f"http://localhost:{port}"
    print(f"\n✓ HTTP server started at {base_url}")

    yield base_url

    # Signal server to stop
    stop_event.set()
    server_thread.join(timeout=2)


# ============================================================================
# Fixtures: Playwright
# ============================================================================


@pytest.fixture(scope="session")
def browser():
    """
    Launch headless Chromium browser via Playwright.

    Yields the browser instance. Closes after all tests.
    """
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        print(f"\n✓ Playwright Chromium launched")
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Create a new browser page for each test."""
    page = browser.new_page()
    yield page
    page.close()


# ============================================================================
# Fixtures: Accessibility (axe-core)
# ============================================================================


@pytest.fixture(scope="session")
def axe_js() -> str:
    """
    Download and cache axe-core.min.js for accessibility testing.

    Returns the JavaScript source code as a string.
    Downloads from CDN once per session and caches in fixtures/ directory.
    """
    FIXTURES_DIR.mkdir(exist_ok=True)
    axe_file = FIXTURES_DIR / "axe.min.js"

    # Return cached version if it exists
    if axe_file.exists():
        with open(axe_file, "r") as f:
            return f.read()

    # Download from CDN
    try:
        print(f"\n↓ Downloading axe-core from {AXECORE_URL}")
        with urllib.request.urlopen(AXECORE_URL, timeout=10) as response:
            axe_code = response.read().decode("utf-8")

        # Cache it
        with open(axe_file, "w") as f:
            f.write(axe_code)

        print(f"✓ axe-core cached at {axe_file}")
        return axe_code
    except Exception as e:
        pytest.fail(f"Failed to download axe-core from CDN: {e}")


# ============================================================================
# Fixtures: File Paths (for unit tests)
# ============================================================================


@pytest.fixture
def data_dir() -> Path:
    """Return path to _data/ directory."""
    return PROJECT_ROOT / "_data"


@pytest.fixture
def publications_dir() -> Path:
    """Return path to _publications/ directory."""
    return PROJECT_ROOT / "_publications"


@pytest.fixture
def pages_dir() -> Path:
    """Return path to _pages/ directory."""
    return PROJECT_ROOT / "_pages"


# ============================================================================
# Pytest Hooks
# ============================================================================


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests")
    config.addinivalue_line("markers", "integration: Integration tests")
    config.addinivalue_line("markers", "acceptance: Acceptance tests")
    config.addinivalue_line("markers", "regression: Regression tests")
    config.addinivalue_line("markers", "e2e: End-to-end tests")


def pytest_collection_modifyitems(config, items):
    """Auto-mark tests based on their directory."""
    for item in items:
        # Determine marker based on file location
        if "unit" in str(item.fspath):
            item.add_marker(pytest.mark.unit)
        elif "integration" in str(item.fspath):
            item.add_marker(pytest.mark.integration)
        elif "acceptance" in str(item.fspath):
            item.add_marker(pytest.mark.acceptance)
        elif "regression" in str(item.fspath):
            item.add_marker(pytest.mark.regression)
        elif "e2e" in str(item.fspath):
            item.add_marker(pytest.mark.e2e)
            item.add_marker(pytest.mark.slow)

        # Mark integration, acceptance, e2e as slow
        if "integration" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
        if "acceptance" in str(item.fspath):
            item.add_marker(pytest.mark.slow)
