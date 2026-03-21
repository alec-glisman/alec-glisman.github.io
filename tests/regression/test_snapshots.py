"""
Regression tests using golden-file snapshots.

Tests that site structure remains unchanged by comparing against stored snapshots.
"""

import json
from pathlib import Path

import pytest


class TestNavigationSnapshot:
    """Test that navigation structure hasn't changed."""

    @pytest.fixture
    def nav_snapshot_dir(self):
        """Create snapshots directory if needed."""
        snap_dir = Path(__file__).parent / "snapshots"
        snap_dir.mkdir(exist_ok=True)
        return snap_dir

    def test_navigation_structure_unchanged(self, data_dir, nav_snapshot_dir):
        """Test that navigation structure matches stored snapshot."""
        import yaml

        nav_file = data_dir / "navigation.yml"
        with open(nav_file) as f:
            nav_data = yaml.safe_load(f)

        # Extract nav structure
        nav_structure = [
            {"title": item["title"], "url": item["url"]}
            for item in nav_data["main"]
        ]

        snapshot_file = nav_snapshot_dir / "navigation.json"

        if snapshot_file.exists():
            # Compare against stored snapshot
            with open(snapshot_file) as f:
                stored_nav = json.load(f)

            assert nav_structure == stored_nav, (
                f"Navigation structure changed!\n"
                f"Expected: {json.dumps(stored_nav, indent=2)}\n"
                f"Got: {json.dumps(nav_structure, indent=2)}"
            )
        else:
            # First run: create snapshot
            with open(snapshot_file, "w") as f:
                json.dump(nav_structure, f, indent=2)
            pytest.skip(f"Snapshot created at {snapshot_file}. Re-run tests to verify.")


class TestPublicationListSnapshot:
    """Test that publication list hasn't changed."""

    @pytest.fixture
    def pub_snapshot_dir(self):
        """Create snapshots directory if needed."""
        snap_dir = Path(__file__).parent / "snapshots"
        snap_dir.mkdir(exist_ok=True)
        return snap_dir

    def test_publication_list_unchanged(self, publications_dir, pub_snapshot_dir):
        """Test that publication list matches stored snapshot."""
        import re
        import yaml

        # Get all publication files
        pub_files = sorted(publications_dir.glob("*.md"))
        pub_list = []

        for pub_file in pub_files:
            # Extract front matter
            content = pub_file.read_text()
            match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if match:
                front_matter = yaml.safe_load(match.group(1))
                pub_list.append({
                    "title": front_matter.get("title"),
                    "permalink": front_matter.get("permalink"),
                })

        snapshot_file = pub_snapshot_dir / "publications.json"

        if snapshot_file.exists():
            # Compare against stored snapshot
            with open(snapshot_file) as f:
                stored_pubs = json.load(f)

            assert pub_list == stored_pubs, (
                f"Publication list changed!\n"
                f"Expected: {json.dumps(stored_pubs, indent=2)}\n"
                f"Got: {json.dumps(pub_list, indent=2)}"
            )
        else:
            # First run: create snapshot
            with open(snapshot_file, "w") as f:
                json.dump(pub_list, f, indent=2)
            pytest.skip(f"Snapshot created at {snapshot_file}. Re-run tests to verify.")


def pytest_addoption(parser):
    """Add --update-snapshots option."""
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update snapshot files",
    )


def pytest_configure(config):
    """Store update-snapshots flag in config."""
    config.update_snapshots = config.getoption("--update-snapshots")
