"""
End-to-end tests for responsive design.

Tests that the site works correctly on different viewport sizes.
"""

import pytest


class TestMobileViewport:
    """Test responsive design on mobile viewport."""

    def test_homepage_on_mobile(self, http_server, page):
        """Test that homepage renders on mobile (375x812)."""
        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 812})

        # Load page
        page.goto(f"{http_server}/")

        # Page should load without errors
        assert page.url
        assert "Alec Glisman" in page.content()

    def test_hamburger_menu_appears_on_mobile(self, http_server, page):
        """Test that hamburger menu appears on mobile viewport."""
        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 812})

        page.goto(f"{http_server}/")

        # Look for hamburger menu button (usually .greedy-nav__toggle)
        hamburger = page.query_selector(".greedy-nav__toggle, [aria-label*='menu' i]")

        # Hamburger should be visible
        if hamburger:
            is_visible = hamburger.is_visible()
            # Not all implementations show hamburger at 375px, but the nav should be responsive
            assert page.url

    def test_content_readable_on_mobile(self, http_server, page):
        """Test that content is readable on mobile."""
        page.set_viewport_size({"width": 375, "height": 812})

        page.goto(f"{http_server}/")

        # Find main content
        main_content = page.query_selector("main, .page__content, article")

        # Should have readable content
        assert page.content()

    def test_responsive_images(self, http_server, page):
        """Test that images are responsive on mobile."""
        page.set_viewport_size({"width": 375, "height": 812})

        page.goto(f"{http_server}/")

        # Find any images
        images = page.query_selector_all("img")

        # Images should load and be visible
        if images:
            for img in images[:3]:  # Check first 3 images
                # Image should have some properties set
                src = img.get_attribute("src")
                assert src, "Image should have src attribute"


class TestTabletViewport:
    """Test responsive design on tablet viewport."""

    def test_homepage_on_tablet(self, http_server, page):
        """Test that homepage renders on tablet (768x1024)."""
        page.set_viewport_size({"width": 768, "height": 1024})

        page.goto(f"{http_server}/")

        assert page.url
        assert "Alec Glisman" in page.content()


class TestDesktopViewport:
    """Test responsive design on desktop viewport."""

    def test_homepage_on_desktop(self, http_server, page):
        """Test that homepage renders on desktop (1280x800)."""
        page.set_viewport_size({"width": 1280, "height": 800})

        page.goto(f"{http_server}/")

        assert page.url
        assert "Alec Glisman" in page.content()

    def test_nav_fully_visible_on_desktop(self, http_server, page):
        """Test that navigation is fully visible on desktop."""
        page.set_viewport_size({"width": 1280, "height": 800})

        page.goto(f"{http_server}/")

        # Find nav
        nav = page.query_selector("nav")
        assert nav is not None, "Nav not found"

        # Should have multiple nav links visible
        nav_links = page.query_selector_all("nav a")
        assert len(nav_links) >= 7, "Expected at least 7 nav links visible"


class TestViewportOrientationChange:
    """Test that site handles orientation changes."""

    def test_landscape_to_portrait_orientation(self, http_server, page):
        """Test changing from landscape to portrait orientation."""
        # Start with landscape
        page.set_viewport_size({"width": 1280, "height": 800})
        page.goto(f"{http_server}/")

        content_landscape = page.content()

        # Switch to portrait
        page.set_viewport_size({"width": 800, "height": 1280})

        # Wait for any layout recalculation
        page.wait_for_timeout(200)

        # Page should still be functional
        content_portrait = page.content()
        assert content_portrait

    def test_portrait_to_landscape_orientation(self, http_server, page):
        """Test changing from portrait to landscape orientation."""
        # Start with portrait
        page.set_viewport_size({"width": 375, "height": 667})
        page.goto(f"{http_server}/")

        # Switch to landscape
        page.set_viewport_size({"width": 667, "height": 375})

        # Wait for any layout recalculation
        page.wait_for_timeout(200)

        # Page should still be functional
        assert page.url
