"""
End-to-end tests for navigation.

Tests full navigation flows using Playwright headless browser.
"""

import pytest


class TestMainNavigation:
    """Test navigation between main pages."""

    def test_navigate_from_homepage_to_publications(self, http_server, page):
        """Test clicking Publications link from homepage."""
        # Load homepage
        page.goto(f"{http_server}/")
        title_before = page.title()

        # Click Publications link
        page.click('a[href="/publications/"]')

        # Verify URL changed
        assert "/publications/" in page.url, f"URL is {page.url}, expected /publications/"

        # Title should change (or at least be different page)
        content = page.content()
        assert "publications" in content.lower(), "Publications page content not found"

    def test_navigate_from_homepage_to_research(self, http_server, page):
        """Test clicking Research link from homepage."""
        page.goto(f"{http_server}/")

        # Click Research link
        page.click('a[href="/research/"]')

        # Verify URL changed
        assert "/research/" in page.url
        assert "Polyelectrolyte" in page.content() or "research" in page.content().lower()

    def test_navigate_from_homepage_to_experience(self, http_server, page):
        """Test clicking Experience link from homepage."""
        page.goto(f"{http_server}/")

        # Click Experience link
        page.click('a[href="/experience/"]')

        # Verify URL changed
        assert "/experience/" in page.url
        assert "experience" in page.content().lower() or "Merck" in page.content()

    def test_navigate_from_homepage_to_projects(self, http_server, page):
        """Test clicking Projects link from homepage."""
        page.goto(f"{http_server}/")

        # Click Projects link
        page.click('a[href="/projects/"]')

        # Verify URL changed
        assert "/projects/" in page.url

    def test_navigate_from_homepage_to_skills(self, http_server, page):
        """Test clicking Skills link from homepage."""
        page.goto(f"{http_server}/")

        # Click Skills link
        page.click('a[href="/skills/"]')

        # Verify URL changed
        assert "/skills/" in page.url


class TestPublicationNavigation:
    """Test navigation to individual publication pages."""

    def test_navigate_to_publication_page(self, http_server, page):
        """Test navigating to a specific publication page."""
        page.goto(f"{http_server}/publications/")

        # Find a publication link (any of the 5)
        pub_link = page.query_selector('a[href*="/publications/2"]')
        assert pub_link is not None, "No publication links found on publications page"

        # Get the href
        href = pub_link.get_attribute("href")

        # Click it
        page.click(f'a[href="{href}"]')

        # Should be on publication page
        assert href.rstrip("/") in page.url

    def test_all_five_publications_are_linked(self, http_server, page):
        """Test that all 5 publications have links on publications page."""
        page.goto(f"{http_server}/publications/")

        pub_links = page.query_selector_all('a[href*="/publications/"]')

        # Should have at least 5 publication links
        pub_links = [
            link for link in pub_links
            if link.get_attribute("href") and
            "/publications/" in link.get_attribute("href") and
            "/publications/index" not in link.get_attribute("href")
        ]

        assert len(pub_links) >= 5, (
            f"Expected at least 5 publication links, found {len(pub_links)}"
        )


class TestBreadcrumbNavigation:
    """Test that users can navigate back."""

    def test_back_button_works(self, http_server, page):
        """Test that browser back button works."""
        # Load homepage
        page.goto(f"{http_server}/")
        home_url = page.url

        # Navigate to publications
        page.goto(f"{http_server}/publications/")
        pub_url = page.url

        # Go back
        page.go_back()

        # Should be back at homepage
        assert home_url in page.url or page.url.rstrip("/") == home_url.rstrip("/")
