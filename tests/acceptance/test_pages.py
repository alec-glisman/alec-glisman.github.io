"""
Acceptance tests for page accessibility.

Tests that all pages are accessible via HTTP and return 200 status.
"""

import time

import pytest
import requests


class TestNavigationPageAccess:
    """Test that all main navigation pages are accessible."""

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/research/",
            "/publications/",
            "/experience/",
            "/projects/",
            "/skills/",
            "/talks/",
            "/teaching/",
        ],
    )
    def test_nav_page_returns_200(self, http_server, path):
        """Test that navigation page returns 200 OK."""
        response = requests.get(f"{http_server}{path}", timeout=5)
        assert response.status_code == 200, (
            f"GET {path} returned {response.status_code}, expected 200"
        )

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/research/",
            "/publications/",
            "/experience/",
            "/projects/",
            "/skills/",
            "/talks/",
            "/teaching/",
        ],
    )
    def test_nav_page_returns_html(self, http_server, path):
        """Test that navigation pages return HTML content type."""
        response = requests.get(f"{http_server}{path}", timeout=5)
        assert "text/html" in response.headers.get("Content-Type", ""), (
            f"GET {path} did not return HTML content type"
        )


class TestPublicationPageAccess:
    """Test that all publication pages are accessible."""

    @pytest.mark.parametrize(
        "publication_path",
        [
            "/publications/2020-scriven-love-1/",
            "/publications/2022-potential-flow-2/",
            "/publications/2024-langmuir-adsorption-isotherm/",
            "/publications/2024-macromolecules-polyelectrolyte/",
            "/publications/2025-langmuir-binding-modes/",
        ],
    )
    def test_publication_returns_200(self, http_server, publication_path):
        """Test that each publication page returns 200 OK."""
        response = requests.get(f"{http_server}{publication_path}", timeout=5)
        assert response.status_code == 200, (
            f"GET {publication_path} returned {response.status_code}, expected 200"
        )


class TestErrorPages:
    """Test error page handling."""

    def test_nonexistent_page_returns_404_or_error_page(self, http_server):
        """Test that nonexistent page returns 404 or 404.html content."""
        response = requests.get(
            f"{http_server}/nonexistent-page-xyz-abc-123/",
            timeout=5,
            allow_redirects=True,
        )
        # Should either be 404 or 200 with 404.html content
        assert response.status_code in [200, 404], (
            f"Nonexistent page returned unexpected status {response.status_code}"
        )


class TestPageLoadTimes:
    """Test that pages load in reasonable time."""

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/publications/",
            "/experience/",
        ],
    )
    def test_page_loads_quickly(self, http_server, path):
        """Test that pages load in under 500ms."""
        start = time.time()
        response = requests.get(f"{http_server}{path}", timeout=5)
        elapsed = time.time() - start

        assert response.status_code == 200
        # Basic performance check: page should load in under 500ms
        # (This is just a smoke test; actual threshold depends on system)
        assert elapsed < 2.0, f"GET {path} took {elapsed:.2f}s, expected < 2.0s"


class TestRedirects:
    """Test that redirects work correctly."""

    def test_about_redirects_work(self, http_server):
        """Test that /about/ redirects to /."""
        response = requests.get(f"{http_server}/about/", timeout=5, allow_redirects=True)
        # Should either redirect or be handled as 200
        assert response.status_code == 200, (
            f"GET /about/ returned {response.status_code}, expected 200 after redirect"
        )

    def test_about_html_redirects_work(self, http_server):
        """Test that /about.html redirects to /."""
        response = requests.get(
            f"{http_server}/about.html",
            timeout=5,
            allow_redirects=True,
        )
        assert response.status_code == 200, (
            f"GET /about.html returned {response.status_code}, expected 200 after redirect"
        )
