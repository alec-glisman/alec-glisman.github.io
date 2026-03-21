"""
Integration tests for page content.

Tests that expected content (text, headings, names) is present on each page.
"""

from bs4 import BeautifulSoup
from pathlib import Path

import pytest


class TestAboutPageContent:
    """Test content on the about/homepage."""

    def test_homepage_contains_author_name(self, site_dir):
        """Test that homepage contains 'Alec Glisman'."""
        homepage = site_dir / "index.html"
        content = homepage.read_text()
        assert "Alec Glisman" in content, "Homepage missing author name"

    def test_homepage_contains_current_role(self, site_dir):
        """Test that homepage mentions Merck and current role."""
        homepage = site_dir / "index.html"
        content = homepage.read_text()
        assert "Merck" in content, "Homepage missing Merck"

    def test_homepage_contains_education(self, site_dir):
        """Test that homepage mentions Caltech PhD."""
        homepage = site_dir / "index.html"
        content = homepage.read_text()
        assert "Caltech" in content, "Homepage missing Caltech"
        assert "PhD" in content, "Homepage missing PhD"


class TestPublicationsPageContent:
    """Test content on the publications page."""

    def test_publications_page_contains_all_titles(self, site_dir):
        """Test that publications page lists all 5 publication titles."""
        pub_page = site_dir / "publications" / "index.html"
        if not pub_page.exists():
            pytest.skip("Publications page not found")

        content = pub_page.read_text()

        expected_titles = [
            "Scriven-Love",  # 2020-scriven-love-1
            "Potential Flow",  # 2022-potential-flow-2
            "Adsorption isotherm",  # 2024-langmuir-adsorption-isotherm
            "Polyelectrolyte Association",  # 2024-macromolecules
            "Binding Modes",  # 2025-langmuir
        ]

        for title in expected_titles:
            assert title in content, f"Publications page missing title: {title}"

    def test_publication_pages_contain_venue(self, site_dir):
        """Test that each publication page contains the journal venue."""
        publication_slugs = [
            ("2020-scriven-love-1", "Physical Review E"),
            ("2022-potential-flow-2", "Journal"),  # JFM Rapids
            ("2024-langmuir-adsorption-isotherm", "Langmuir"),
            ("2024-macromolecules-polyelectrolyte", "Macromolecules"),
            ("2025-langmuir-binding-modes", "Langmuir"),
        ]

        for slug, expected_venue in publication_slugs:
            pub_page = site_dir / "publications" / slug / "index.html"
            if not pub_page.exists():
                pytest.skip(f"Publication page not found: {slug}")

            content = pub_page.read_text()
            assert expected_venue in content, (
                f"Publication page {slug} missing venue: {expected_venue}"
            )


class TestExperiencePageContent:
    """Test content on the experience page."""

    def test_experience_page_contains_current_role(self, site_dir):
        """Test that experience page mentions Senior ML Scientist at Merck."""
        exp_page = site_dir / "experience" / "index.html"
        if not exp_page.exists():
            pytest.skip("Experience page not found")

        content = exp_page.read_text()
        assert "Senior ML Scientist" in content, (
            "Experience page missing 'Senior ML Scientist'"
        )
        assert "Merck" in content, "Experience page missing Merck"

    def test_experience_page_lists_employers(self, site_dir):
        """Test that experience page mentions previous employers."""
        exp_page = site_dir / "experience" / "index.html"
        if not exp_page.exists():
            pytest.skip("Experience page not found")

        content = exp_page.read_text()

        employers = ["Caltech", "Nissan", "Bosch"]
        for employer in employers:
            assert employer in content, (
                f"Experience page missing employer: {employer}"
            )


class TestProjectsPageContent:
    """Test content on the projects page."""

    def test_projects_page_contains_project_names(self, site_dir):
        """Test that projects page lists the main projects."""
        projects_page = site_dir / "projects" / "index.html"
        if not projects_page.exists():
            pytest.skip("Projects page not found")

        content = projects_page.read_text()

        expected_projects = [
            "DDPM",
            "OpenADMET",
            "Polyelectrolyte",  # Analysis-Polyelectrolyte
        ]

        for project in expected_projects:
            assert project in content, f"Projects page missing project: {project}"


class TestSkillsPageContent:
    """Test content on the skills page."""

    def test_skills_page_contains_major_skills(self, site_dir):
        """Test that skills page lists major technical skills."""
        skills_page = site_dir / "skills" / "index.html"
        if not skills_page.exists():
            pytest.skip("Skills page not found")

        content = skills_page.read_text()

        expected_skills = [
            "PyTorch",
            "Python",
            "GROMACS",
        ]

        for skill in expected_skills:
            assert skill in content, f"Skills page missing skill: {skill}"


class TestResearchPageContent:
    """Test content on the research page."""

    def test_research_page_has_three_themes(self, site_dir):
        """Test that research page describes three research areas."""
        research_page = site_dir / "research" / "index.html"
        if not research_page.exists():
            pytest.skip("Research page not found")

        content = research_page.read_text()

        # The three research themes mentioned in DESIGN_OVERVIEW.md
        themes = [
            "Polyelectrolyte",
            "Microhydrodynamics",
            "Membrane",  # Lipid Membrane Mechanics
        ]

        for theme in themes:
            assert theme in content, f"Research page missing theme: {theme}"

    def test_research_page_links_to_publications(self, site_dir):
        """Test that research page links to related publications."""
        research_page = site_dir / "research" / "index.html"
        if not research_page.exists():
            pytest.skip("Research page not found")

        soup = BeautifulSoup(research_page.read_text(), "html.parser")
        links = soup.find_all("a", href=True)
        publication_links = [
            link for link in links
            if "/publications/" in link.get("href")
        ]

        assert len(publication_links) > 0, (
            "Research page should have links to publications"
        )
