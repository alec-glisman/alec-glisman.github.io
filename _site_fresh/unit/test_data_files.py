"""
Unit tests for YAML data files.

Tests that _data/*.yml files are valid YAML and contain required fields.
"""

import pytest
import yaml


class TestNavigationData:
    """Verify _data/navigation.yml is valid and complete."""

    def test_navigation_yaml_parses(self, data_dir):
        """Test that navigation.yml is valid YAML."""
        nav_file = data_dir / "navigation.yml"
        assert nav_file.exists(), "navigation.yml not found"
        with open(nav_file) as f:
            data = yaml.safe_load(f)
        assert data is not None, "navigation.yml is empty or invalid"

    def test_navigation_has_main_menu(self, data_dir):
        """Test that navigation has 'main' menu."""
        nav_file = data_dir / "navigation.yml"
        with open(nav_file) as f:
            data = yaml.safe_load(f)
        assert "main" in data, "navigation.yml missing 'main' key"
        assert isinstance(data["main"], list), "main should be a list"

    def test_navigation_menu_items_count(self, data_dir):
        """Test that navigation menu has exactly 7 items."""
        nav_file = data_dir / "navigation.yml"
        with open(nav_file) as f:
            data = yaml.safe_load(f)
        assert len(data["main"]) == 7, f"Expected 7 nav items, got {len(data['main'])}"

    def test_navigation_menu_items_have_required_fields(self, data_dir):
        """Test that each nav item has 'title' and 'url' fields."""
        nav_file = data_dir / "navigation.yml"
        with open(nav_file) as f:
            data = yaml.safe_load(f)
        for i, item in enumerate(data["main"]):
            assert "title" in item, f"Nav item {i} missing 'title'"
            assert "url" in item, f"Nav item {i} missing 'url'"
            assert item["title"], f"Nav item {i} has empty title"
            assert item["url"], f"Nav item {i} has empty url"

    def test_navigation_urls_are_correct(self, data_dir):
        """Test that navigation URLs match expected values."""
        nav_file = data_dir / "navigation.yml"
        with open(nav_file) as f:
            data = yaml.safe_load(f)

        expected_urls = {
            "/research/",
            "/publications/",
            "/experience/",
            "/projects/",
            "/skills/",
            "/talks/",
            "/teaching/",
        }

        actual_urls = {item["url"] for item in data["main"]}
        assert actual_urls == expected_urls, f"Nav URLs mismatch.\nExpected: {expected_urls}\nActual: {actual_urls}"


class TestAuthorsData:
    """Verify _data/authors.yml is valid and complete."""

    def test_authors_yaml_parses(self, data_dir):
        """Test that authors.yml is valid YAML."""
        authors_file = data_dir / "authors.yml"
        assert authors_file.exists(), "authors.yml not found"
        with open(authors_file) as f:
            data = yaml.safe_load(f)
        assert data is not None, "authors.yml is empty or invalid"

    def test_authors_has_me_entry(self, data_dir):
        """Test that authors.yml has 'Me' entry."""
        authors_file = data_dir / "authors.yml"
        with open(authors_file) as f:
            data = yaml.safe_load(f)
        assert "Me" in data, "authors.yml missing 'Me' author"

    def test_author_has_required_fields(self, data_dir):
        """Test that 'Me' author has required fields."""
        authors_file = data_dir / "authors.yml"
        with open(authors_file) as f:
            data = yaml.safe_load(f)

        author = data["Me"]
        required_fields = ["name", "uri", "bio", "email"]
        for field in required_fields:
            assert field in author, f"Author 'Me' missing field: {field}"
            assert author[field], f"Author 'Me' has empty {field}"

    def test_author_uri_is_not_template_default(self, data_dir):
        """Test that author URI is not the template default 'http://name.com'."""
        authors_file = data_dir / "authors.yml"
        with open(authors_file) as f:
            data = yaml.safe_load(f)

        uri = data["Me"]["uri"]
        assert uri != "http://name.com", "Author URI is still the template default"
        assert "alec-glisman.github.io" in uri, "Author URI should reference the site"

    def test_author_name_is_alec_glisman(self, data_dir):
        """Test that author name is 'Alec Glisman'."""
        authors_file = data_dir / "authors.yml"
        with open(authors_file) as f:
            data = yaml.safe_load(f)

        name = data["Me"]["name"]
        assert "Alec Glisman" in name, f"Author name should include 'Alec Glisman', got {name}"
