"""
Unit tests for publication front matter.

Tests that all publication markdown files have valid YAML front matter
with required fields and no duplicates.
"""

import re
from pathlib import Path

import pytest
import yaml


def parse_front_matter(md_file: Path) -> dict:
    """Parse YAML front matter from a markdown file."""
    content = md_file.read_text()
    # Front matter is between --- delimiters
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        raise ValueError(f"No front matter found in {md_file}")
    front_matter_str = match.group(1)
    return yaml.safe_load(front_matter_str)


class TestPublicationFrontMatter:
    """Verify all publications have valid front matter."""

    @pytest.fixture
    def publication_files(self, publications_dir) -> list:
        """Get all publication markdown files."""
        return sorted(publications_dir.glob("*.md"))

    def test_publication_count(self, publication_files):
        """Test that exactly 5 publications exist."""
        assert len(publication_files) == 5, f"Expected 5 publications, found {len(publication_files)}"

    def test_all_publications_have_yaml_frontmatter(self, publication_files):
        """Test that all publication files have valid YAML front matter."""
        for pub_file in publication_files:
            # Should not raise
            front_matter = parse_front_matter(pub_file)
            assert front_matter is not None, f"{pub_file.name} has invalid front matter"

    @pytest.mark.parametrize(
        "required_field",
        [
            "title",
            "collection",
            "permalink",
            "excerpt",
            "date",
            "venue",
            "paperurl",
            "citation",
        ],
    )
    def test_all_publications_have_required_field(self, publication_files, required_field):
        """Test that all publications have required fields."""
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            assert required_field in front_matter, (
                f"{pub_file.name} missing field '{required_field}'"
            )
            assert front_matter[required_field], (
                f"{pub_file.name} has empty field '{required_field}'"
            )

    def test_collection_is_publications(self, publication_files):
        """Test that collection field is 'publications' for all."""
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            assert front_matter["collection"] == "publications", (
                f"{pub_file.name} collection should be 'publications', got {front_matter['collection']}"
            )

    def test_no_duplicate_permalinks(self, publication_files):
        """Test that no two publications share the same permalink."""
        permalinks = []
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            permalinks.append(front_matter["permalink"])

        assert len(permalinks) == len(set(permalinks)), (
            f"Duplicate permalinks found: {[p for p in permalinks if permalinks.count(p) > 1]}"
        )

    def test_no_duplicate_titles(self, publication_files):
        """Test that no two publications share the same title."""
        titles = []
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            titles.append(front_matter["title"])

        assert len(titles) == len(set(titles)), (
            f"Duplicate titles found: {[t for t in titles if titles.count(t) > 1]}"
        )

    def test_dates_are_valid(self, publication_files):
        """Test that publication dates are parseable as dates."""
        import re
        from datetime import datetime, date

        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            date_val = front_matter["date"]

            # Should be a date string (YYYY-MM-DD), datetime.date, or datetime object
            if isinstance(date_val, str):
                # Check if it looks like a date (basic pattern)
                if not re.match(r'^\d{4}-\d{2}-\d{2}', date_val):
                    pytest.fail(f"{pub_file.name} has invalid date format: {date_val} (expected YYYY-MM-DD)")
            elif isinstance(date_val, (datetime, date)):
                # YAML parser auto-converts YYYY-MM-DD to datetime.date objects - that's fine
                pass
            else:
                pytest.fail(f"{pub_file.name} has unexpected date type: {type(date_val)}")

    def test_excerpts_are_unique(self, publication_files):
        """Test that publication excerpts are unique (no copy-paste duplicates)."""
        excerpts = []
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            excerpts.append(front_matter["excerpt"])

        assert len(excerpts) == len(set(excerpts)), (
            f"Duplicate excerpts found (likely copy-paste errors)."
        )

    def test_paperurl_is_valid_url(self, publication_files):
        """Test that paperurl values are valid HTTPS URLs."""
        for pub_file in publication_files:
            front_matter = parse_front_matter(pub_file)
            url = front_matter["paperurl"]
            # Should be HTTPS URL
            assert url.startswith("https://"), (
                f"{pub_file.name} paperurl should start with https://, got {url}"
            )
            # Should contain expected publication patterns
            assert any(pattern in url for pattern in [
                "doi.org/",
                "journals.",
                "arxiv",
                "researchgate",
            ]), (
                f"{pub_file.name} paperurl doesn't match expected patterns: {url}"
            )
