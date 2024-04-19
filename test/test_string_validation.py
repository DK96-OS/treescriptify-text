"""Testing String Validation Methods
"""
import pytest
from treescriptify_text.string_validation import validate_name


@pytest.mark.parametrize(
    "test_input,expect",
    [
        (None, False),
        (4, False),
        ({}, False),
        ([], False),
        ("", False),
        (" ", False),
        ("\n", False),
    ]
)
def test_validate_name_returns_false(test_input, expect):
    assert validate_name(test_input) == expect


@pytest.mark.parametrize(
    "test_input,expect",
    [
        ("1", True),
        ("a", True),
        ("test", True),
    ]
)
def test_validate_name_returns_true(test_input, expect):
    assert validate_name(test_input) == expect
