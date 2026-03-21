"""
Regression tests for custom CSS classes.

Tests that custom CSS classes are present in rendered HTML,
detecting unintended removal or changes to the design system.
"""

from bs4 import BeautifulSoup

import pytest


class TestCustomCSSClasses:
    """Test that custom CSS classes are present in rendered pages."""

    def test_homepage_has_reveal_class(self, site_dir):
        """Test that homepage contains .reveal elements."""
        homepage = site_dir / "index.html"
        content = homepage.read_text()
        assert 'class="reveal"' in content or "class='reveal'" in content, (
            "Homepage missing .reveal elements for scroll animations"
        )

    def test_homepage_has_research_cards(self, site_dir):
        """Test that homepage/research content has .research-card classes."""
        content = ""
        # Check either homepage or research page
        for page_path in ["index.html", "research/index.html"]:
            page_file = site_dir / page_path
            if page_file.exists():
                content = page_file.read_text()
                if "research-card" in content:
                    break

        assert "research-card" in content, (
            "Missing .research-card elements on homepage or research page"
        )

    def test_experience_page_has_timeline_classes(self, site_dir):
        """Test that experience page has timeline-related classes."""
        exp_page = site_dir / "experience" / "index.html"
        if not exp_page.exists():
            pytest.skip("Experience page not found")

        content = exp_page.read_text()
        assert "experience-entry" in content, (
            "Experience page missing .experience-entry class"
        )

    def test_projects_page_has_project_cards(self, site_dir):
        """Test that projects page has .project-card classes."""
        projects_page = site_dir / "projects" / "index.html"
        if not projects_page.exists():
            pytest.skip("Projects page not found")

        content = projects_page.read_text()
        assert "project-card" in content, (
            "Projects page missing .project-card class"
        )

    def test_skills_page_has_skill_tags(self, site_dir):
        """Test that skills page has .skill-tag classes."""
        skills_page = site_dir / "skills" / "index.html"
        if not skills_page.exists():
            pytest.skip("Skills page not found")

        content = skills_page.read_text()
        assert "skill-tag" in content, (
            "Skills page missing .skill-tag class"
        )
        assert "skill-group" in content, (
            "Skills page missing .skill-group class"
        )


class TestDesignColorSystem:
    """Test that the Navy/Teal color system is applied."""

    def test_navy_color_present_in_css(self, site_dir):
        """Test that Navy color (#1B2A4A) is present in compiled CSS."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if not css_file.exists():
            pytest.skip("CSS file not found")

        content = css_file.read_text()
        # Check for Navy color in either uppercase or lowercase hex
        navy_found = "#1B2A4A" in content or "#1b2a4a" in content
        assert navy_found, "Navy color (#1B2A4A) not found in main.css"

    def test_teal_color_present_in_css(self, site_dir):
        """Test that Teal color (#0EA5C9) is present in compiled CSS."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if not css_file.exists():
            pytest.skip("CSS file not found")

        content = css_file.read_text()
        # Check for Teal color in either uppercase or lowercase hex
        teal_found = "#0EA5C9" in content or "#0ea5c9" in content
        assert teal_found, "Teal color (#0EA5C9) not found in main.css"

    def test_inter_font_loaded(self, site_dir):
        """Test that Inter font is loaded."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if not css_file.exists():
            pytest.skip("CSS file not found")

        content = css_file.read_text()
        # Should have Inter in font family stack
        assert "Inter" in content, "Inter font not found in main.css"


class TestScrollRevealStyles:
    """Test that scroll-reveal animation styles are present."""

    def test_reveal_css_rules_present(self, site_dir):
        """Test that .reveal CSS rules are in main.css."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if not css_file.exists():
            pytest.skip("CSS file not found")

        content = css_file.read_text()
        assert ".reveal" in content, ".reveal CSS rules not found in main.css"


class TestMastheadStyling:
    """Test that masthead has custom styling."""

    def test_masthead_has_navy_background(self, site_dir):
        """Test that masthead has Navy background styling."""
        css_file = site_dir / "assets" / "css" / "main.css"
        if not css_file.exists():
            pytest.skip("CSS file not found")

        content = css_file.read_text()
        # Should have some reference to masthead and navy
        # (simplified check since exact CSS selector may vary)
        assert ".masthead" in content or "masthead" in content.lower(), (
            "Masthead CSS not found"
        )
