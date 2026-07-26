import json
from pathlib import Path


def test_output_exists():
    """The agent must write /app/output.json."""
    assert Path("/app/output.json").exists()


def test_output_schema():
    """Verify that /app/output.json contains the required schema keys."""
    data = json.loads(Path("/app/output.json").read_text())
    assert {"input_rows", "output_rows", "duplicates_removed"} <= data.keys()
