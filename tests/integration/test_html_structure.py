"""
Integration tests for HTML structure.

Tests that generated HTML pages have proper structure, meta tags, and elements.
"""

from bs4 import BeautifulSoup
from pathlib import Path

import pytest


def get_html_files(site_dir: Path) -> list:
    """Get all index.html files from _site/."""
    return sorted(site_dir.glob("**/index.html"))


@pytest.fixture
def html_files(site_dir):
    """Get all HTML files in the site."""
    return get_html_files(site_dir)


class TestHTMLBasicStructure:
    """Test basic HTML structure on all pages."""

    def test_all_pages_have_html_element(self, html_files):
        """Test that all pages have <html> tag."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            html_tag = soup.find("html")
            assert html_tag is not None, f"{html_file} missing <html> tag"

    def test_all_pages_have_lang_attribute(self, html_files):
        """Test that all <html> tags have lang='en' attribute."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            html_tag = soup.find("html")
            assert "lang" in html_tag.attrs, f"{html_file} <html> missing lang attribute"
            assert html_tag.attrs["lang"] == "en", (
                f"{html_file} lang should be 'en', got {html_tag.attrs['lang']}"
            )

    def test_all_pages_have_title(self, html_files):
        """Test that all pages have <title> tag."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            title_tag = soup.find("title")
            assert title_tag is not None, f"{html_file} missing <title> tag"
            assert title_tag.string and title_tag.string.strip(), (
                f"{html_file} <title> is empty"
            )

    def test_all_pages_have_description_meta(self, html_files):
        """Test that all pages have meta description."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            desc = soup.find("meta", {"name": "description"})
            assert desc is not None, f"{html_file} missing meta description"
            assert desc.get("content"), f"{html_file} meta description is empty"


class TestMastheadNavigation:
    """Test masthead and navigation structure."""

    def test_pages_have_masthead_nav(self, html_files):
        """Test that pages have <nav> in masthead."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            nav = soup.find("nav")
            assert nav is not None, f"{html_file} missing <nav> tag"

    def test_nav_contains_all_menu_items(self, html_files, site_dir):
        """Test that nav contains links to all 7 navigation items."""
        expected_nav_urls = {
            "/research/",
            "/publications/",
            "/experience/",
            "/projects/",
            "/skills/",
            "/talks/",
            "/teaching/",
        }

        # Check at least one HTML file (the homepage should have all nav items)
        for html_file in html_files:
            if "index.html" == html_file.name and html_file.parent == site_dir:
                # This is the homepage
                soup = BeautifulSoup(html_file.read_text(), "html.parser")
                nav = soup.find("nav")
                nav_links = nav.find_all("a", href=True)
                nav_hrefs = {link.get("href") for link in nav_links}

                for expected_url in expected_nav_urls:
                    assert expected_url in nav_hrefs, (
                        f"Homepage nav missing link to {expected_url}. "
                        f"Found: {nav_hrefs}"
                    )


class TestFooter:
    """Test footer presence."""

    def test_pages_have_footer(self, html_files):
        """Test that pages have <footer> tag."""
        for html_file in html_files:
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            footer = soup.find("footer")
            assert footer is not None, f"{html_file} missing <footer> tag"


class TestFontLoading:
    """Test that custom fonts are loaded."""

    def test_inter_font_is_linked(self, site_dir):
        """Test that Inter font is loaded from Google Fonts."""
        homepage = site_dir / "index.html"
        soup = BeautifulSoup(homepage.read_text(), "html.parser")

        # Look for link tags
        font_links = soup.find_all("link", href=True)
        inter_found = any(
            "fonts.googleapis.com" in link.get("href") and "Inter" in link.get("href")
            for link in font_links
        )
        assert inter_found, "Inter font link not found in <head>"


class TestThemeColors:
    """Test that custom theme colors are applied."""

    def test_navy_color_in_styles(self, site_dir):
        """Test that Navy color (#1B2A4A) is in CSS."""
        # CSS should be available after build
        css_file = site_dir / "assets" / "css" / "main.css"
        if css_file.exists():
            css_content = css_file.read_text()
            assert "#1B2A4A" in css_content or "#1b2a4a" in css_content, (
                "Navy color (#1B2A4A) not found in main.css"
            )

    def test_teal_color_in_styles(self, site_dir):
        """Test that Teal color (#0EA5C9) is in CSS."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if css_file.exists():
            css_content = css_file.read_text()
            assert "#0EA5C9" in css_content or "#0ea5c9" in css_content, (
                "Teal color (#0EA5C9) not found in main.css"
            )
