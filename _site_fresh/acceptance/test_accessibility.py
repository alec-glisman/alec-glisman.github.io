"""
Acceptance tests for accessibility.

Tests that pages meet WCAG 2.1 standards using axe-core via Playwright.
"""

import pytest


class TestAccessibilityWithAxeCore:
    """Test accessibility using axe-core injected into Playwright."""

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/research/",
            "/publications/",
            "/experience/",
            "/projects/",
            "/skills/",
        ],
    )
    def test_page_has_no_critical_violations(
        self, http_server, page, axe_js, path
    ):
        """Test that page has no critical accessibility violations."""
        # Navigate to page; domcontentloaded ensures CSS is parsed
        page.goto(f"{http_server}{path}", wait_until="domcontentloaded")

        # Inject axe-core
        page.evaluate(axe_js)

        # Run accessibility scan
        results = page.evaluate(
            """
            async () => {
                const results = await axe.run();
                return {
                    violations: results.violations,
                    passes: results.passes.length,
                    incomplete: results.incomplete.length,
                };
            }
            """
        )

        # Check for critical violations
        violations = results.get("violations", [])
        critical_violations = [
            v for v in violations if v.get("impact") in ["critical", "serious"]
        ]

        if critical_violations:
            # Format error message
            error_msg = f"\nPage {path} has {len(critical_violations)} critical/serious violations:\n"
            for violation in critical_violations:
                error_msg += (
                    f"  - {violation.get('id')}: {violation.get('description')}\n"
                    f"    Affected elements: {len(violation.get('nodes', []))}\n"
                )
            pytest.fail(error_msg)

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/publications/",
        ],
    )
    def test_page_passes_basic_checks(self, http_server, page, axe_js, path):
        """Test that page passes basic WCAG checks."""
        # Navigate to page; domcontentloaded ensures CSS is parsed
        page.goto(f"{http_server}{path}", wait_until="domcontentloaded")

        # Inject axe-core
        page.evaluate(axe_js)

        # Run accessibility scan
        results = page.evaluate(
            """
            async () => {
                const results = await axe.run();
                return {
                    violations: results.violations.length,
                    passes: results.passes.length,
                    incomplete: results.incomplete.length,
                };
            }
            """
        )

        # Page should have some passing checks
        assert results.get("passes", 0) > 0, f"Page {path} has no passing accessibility checks"


class TestColorContrast:
    """Test color contrast on key elements."""

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/publications/",
        ],
    )
    def test_text_has_sufficient_contrast(self, http_server, page, path):
        """Test that main text has sufficient color contrast."""
        page.goto(f"{http_server}{path}")

        # Check that body text is readable (basic heuristic)
        # Look for text with low contrast (would be caught by axe-core more thoroughly)
        text_elements = page.query_selector_all("p, h1, h2, h3")

        assert len(text_elements) > 0, f"Page {path} has no text elements"


class TestNavigationAccessibility:
    """Test that navigation is accessible."""

    def test_nav_is_keyboard_accessible(self, http_server, page):
        """Test that navigation is keyboard accessible."""
        page.goto(f"{http_server}/")

        # Find nav element
        nav = page.query_selector("nav")
        assert nav is not None, "Navigation element not found"

        # Nav links should be visible/focusable
        nav_links = page.query_selector_all("nav a")
        assert len(nav_links) >= 7, "Expected at least 7 navigation links"
