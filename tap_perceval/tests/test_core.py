"""Tests standard tap features using the built-in SDK tests library."""

import json
from pathlib import Path

from singer_sdk.testing import get_standard_tap_tests

from tap_perceval.tap import TapPerceval

PROJECT_ROOT = Path(__file__).parents[2]
with open(PROJECT_ROOT / "sample_config.json") as f:
    SAMPLE_CONFIG = json.load(f)


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(
        TapPerceval,
        config=SAMPLE_CONFIG
    )
    for test in tests:
        test()
