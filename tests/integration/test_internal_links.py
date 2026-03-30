"""
Integration tests for internal link integrity.

Tests that all internal links in the site resolve to existing files.
"""

from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urlparse

import pytest


def resolve_link(html_file: Path, href: str, site_dir: Path) -> Path | None:
    """
    Resolve a relative href to an absolute path in _site/.

    Args:
        html_file: Path to the HTML file containing the link
        href: The href value (relative or absolute)
        site_dir: Path to _site/ directory

    Returns:
        Resolved path if resolvable, None if external link
    """
    # Skip absolute URLs and anchors
    if href.startswith("http://") or href.startswith("https://"):
        return None
    if href.startswith("#"):
        return None
    if href.startswith("mailto:"):
        return None

    # Strip fragment identifier before resolving path
    href = href.split("#")[0]

    # Relative to site root
    if href.startswith("/"):
        path = site_dir / href.lstrip("/")
    else:
        # Relative to current file
        path = html_file.parent / href

    # Normalize the path
    path = path.resolve()

    # If it's a directory, check for index.html
    if path.is_dir():
        path = path / "index.html"

    return path if path.exists() else None


class TestInternalLinkResolution:
    """Test that internal links resolve to existing files."""

    def test_all_internal_links_resolve(self, site_dir):
        """Test that all internal hrefs point to existing files."""
        broken_links = []

        for html_file in site_dir.glob("**/index.html"):
            soup = BeautifulSoup(html_file.read_text(), "html.parser")
            links = soup.find_all("a", href=True)

            for link in links:
                href = link.get("href")

                # Skip external links
                if href.startswith("http://") or href.startswith("https://"):
                    continue
                if href.startswith("mailto:"):
                    continue
                if href.startswith("#"):
                    continue

                # Try to resolve
                resolved = resolve_link(html_file, href, site_dir)

                # Check if it's an external link (CDN, etc.)
                parsed_url = urlparse(href)
                if parsed_url.netloc:
                    continue  # External link, skip

                if resolved is None:
                    broken_links.append(
                        {
                            "file": str(html_file.relative_to(site_dir)),
                            "href": href,
                        }
                    )

        assert len(broken_links) == 0, (
            f"Found {len(broken_links)} broken internal links:\n"
            + "\n".join(f"  {b['file']}: {b['href']}" for b in broken_links)
        )

    def test_nav_links_are_accessible(self, site_dir):
        """Test that main navigation links are accessible."""
        homepage = site_dir / "index.html"
        soup = BeautifulSoup(homepage.read_text(), "html.parser")

        nav = soup.find("nav")
        nav_links = nav.find_all("a", href=True) if nav else []

        for link in nav_links:
            href = link.get("href")
            if not href or href.startswith("http"):
                continue

            target_path = site_dir / href.lstrip("/")
            if target_path.is_dir():
                target_path = target_path / "index.html"

            assert target_path.exists(), f"Nav link broken: {href} -> {target_path}"


class TestPublicationLinkTargets:
    """Test that publication links point to valid pages."""

    def test_publication_links_on_publications_page(self, site_dir):
        """Test that links from /publications/ page point to publication pages."""
        pub_index = site_dir / "publications" / "index.html"
        if not pub_index.exists():
            pytest.skip("Publications page not found")

        soup = BeautifulSoup(pub_index.read_text(), "html.parser")
        links = soup.find_all("a", href=True)

        for link in links:
            href = link.get("href")
            if not href or not href.startswith("/publications/"):
                continue

            target = site_dir / href.lstrip("/")
            if target.is_dir():
                target = target / "index.html"

            assert target.exists(), (
                f"Publication link broken on /publications/: {href}"
            )

    def test_all_5_publications_are_linked(self, site_dir):
        """Test that all 5 publications are linked from /publications/ page."""
        pub_index = site_dir / "publications" / "index.html"
        if not pub_index.exists():
            pytest.skip("Publications page not found")

        content = pub_index.read_text().lower()

        # Check for DOI identifiers — these uniquely identify each publication
        # and are present as href links on the hand-written publications page.
        expected_dois = {
            "10.1103/physreve.101.052401",       # 2020 Scriven-Love
            "10.1017/jfm.2022.946",              # 2022 Potential Flow
            "10.1021/acs.langmuir.3c03812",      # 2024 Adsorption Isotherm
            "10.1021/acs.macromol.3c02103",       # 2024 Macromolecules
            "10.1021/acs.langmuir.4c03301",      # 2025 Binding Modes
        }

        for doi in expected_dois:
            assert doi in content, f"Publication DOI not found on /publications/ page: {doi}"
