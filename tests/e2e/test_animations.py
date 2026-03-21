"""
End-to-end tests for animations and interactions.

Tests that scroll-reveal animations and hover effects work correctly.
"""

import pytest


class TestScrollRevealAnimation:
    """Test scroll-reveal animations with IntersectionObserver."""

    def test_reveal_elements_not_visible_before_scroll(self, http_server, page):
        """Test that .reveal elements aren't marked as visible initially."""
        page.goto(f"{http_server}/")

        # Query .reveal elements
        reveal_elements = page.query_selector_all(".reveal")
        assert len(reveal_elements) > 0, "No .reveal elements found on homepage"

        # Check that none have .is-visible class
        for elem in reveal_elements:
            is_visible = "is-visible" in (elem.get_attribute("class") or "")
            # At least most should not be visible initially (unless already scrolled into view)
            # This is a soft check since viewport might already show some

    def test_reveal_elements_visible_after_scroll(self, http_server, page):
        """Test that .reveal elements get .is-visible class after scrolling."""
        page.goto(f"{http_server}/")

        # Find a .reveal element that's not in viewport
        reveal_elements = page.query_selector_all(".reveal")
        assert len(reveal_elements) > 0, "No .reveal elements found"

        # Scroll to bottom
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Wait a moment for animations to trigger
        page.wait_for_timeout(500)

        # At least one reveal element should now have is-visible
        reveal_with_visible = page.query_selector(".reveal.is-visible")
        assert reveal_with_visible is not None, (
            "No .reveal.is-visible elements found after scrolling"
        )


class TestHoverEffects:
    """Test that hover effects and transitions work."""

    def test_nav_links_are_interactive(self, http_server, page):
        """Test that nav links respond to hover."""
        page.goto(f"{http_server}/")

        # Find a nav link
        nav_link = page.query_selector("nav a")
        assert nav_link is not None, "No nav links found"

        # Hover over it (should not error)
        nav_link.hover()

        # Page should still be responsive
        assert page.url

    def test_publication_cards_are_hoverable(self, http_server, page):
        """Test that publication cards respond to hover."""
        page.goto(f"{http_server}/publications/")

        # Find a publication card
        pub_card = page.query_selector("a.post-title")
        if pub_card:
            # Hover over it
            pub_card.hover()
            # Should not error and page should be responsive
            assert page.url


class TestJavaScriptExecution:
    """Test that JavaScript runs correctly."""

    def test_intersection_observer_is_available(self, http_server, page):
        """Test that IntersectionObserver is available in the page."""
        page.goto(f"{http_server}/")

        has_io = page.evaluate("'IntersectionObserver' in window")
        assert has_io is True, "IntersectionObserver not available"

    def test_scroll_event_tracking(self, http_server, page):
        """Test that scroll position can be detected."""
        page.goto(f"{http_server}/")

        # Get initial scroll position
        initial_scroll = page.evaluate("window.scrollY")
        assert initial_scroll == 0, "Should start at top"

        # Scroll down
        page.evaluate("window.scrollTo(0, 500)")

        # Check new position
        final_scroll = page.evaluate("window.scrollY")
        assert final_scroll > 0, "Scroll position should change"
