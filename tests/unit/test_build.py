"""
Unit tests for Jekyll build process.

Tests that the Jekyll site builds successfully without errors or warnings.
"""

import pytest


class TestBuildProcess:
    """Verify Jekyll build completes successfully."""

    def test_site_builds_without_errors(self, site_dir):
        """Test that site_dir fixture successfully builds the site."""
        # The site_dir fixture runs 'bundle exec jekyll build'
        # If we reach this test, the build succeeded (fixture would have failed otherwise)
        assert site_dir.exists(), "Jekyll build did not create _site directory"

    def test_site_directory_is_not_empty(self, site_dir):
        """Test that _site/ directory contains files."""
        files = list(site_dir.glob("*"))
        assert len(files) > 0, "_site/ directory is empty"


class TestBuildOutputStructure:
    """Verify expected files exist in built output."""

    @pytest.mark.parametrize(
        "expected_file",
        [
            "index.html",  # Homepage (about page)
            "research/index.html",
            "publications/index.html",
            "experience/index.html",
            "projects/index.html",
            "skills/index.html",
            "talks/index.html",
            "teaching/index.html",
            "assets/css/main.css",
            "assets/js/main.min.js",
        ],
    )
    def test_expected_pages_exist(self, site_dir, expected_file):
        """Test that expected pages are built."""
        file_path = site_dir / expected_file
        assert file_path.exists(), f"Expected file not found: {expected_file}"
        assert file_path.stat().st_size > 0, f"File is empty: {expected_file}"


class TestPublicationPages:
    """Verify all 5 publication pages exist."""

    @pytest.mark.parametrize(
        "publication_slug",
        [
            "2020-scriven-love-1",
            "2022-potential-flow-2",
            "2024-langmuir-adsorption-isotherm",
            "2024-macromolecules-polyelectrolyte",
            "2025-langmuir-binding-modes",
        ],
    )
    def test_publication_pages_exist(self, site_dir, publication_slug):
        """Test that each publication has a built HTML page."""
        pub_path = site_dir / "publications" / publication_slug / "index.html"
        assert pub_path.exists(), f"Publication page missing: {publication_slug}"
        assert pub_path.stat().st_size > 0, f"Publication page is empty: {publication_slug}"


class TestAssetFiles:
    """Verify compiled CSS and JS assets exist."""

    def test_css_compiled(self, site_dir):
        """Test that main.css is compiled and non-empty."""
        css_file = site_dir / "assets" / "css" / "main.css"
        assert css_file.exists(), "CSS file not found"
        content = css_file.read_text()
        assert len(content) > 1000, "CSS file seems too small to be complete"

    def test_js_minified(self, site_dir):
        """Test that main.min.js exists."""
        js_file = site_dir / "assets" / "js" / "main.min.js"
        assert js_file.exists(), "JavaScript file not found"
        # JavaScript file should have some content
        content = js_file.read_text()
        assert len(content) > 0, "JavaScript file is empty"
