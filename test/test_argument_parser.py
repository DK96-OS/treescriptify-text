"""Testing Module Methods
"""
from pathlib import Path
import pytest

from treescriptify_text.input_data import InputData
from treescriptify_text.argument_parser import parse_args


@pytest.mark.parametrize(
    'test_input,expected',
    [
        (['tree_file'], InputData(tree_text='file_data')),
        (['tree_file', '-d'], InputData(tree_text='file_data', directories_only=True)),
    ]
)
def test_parse_args_returns_input(test_input, expected):
    with pytest.MonkeyPatch().context() as c:
        c.setattr(Path, 'exists', lambda _: True)
        c.setattr(Path, 'read_text', lambda _: "file_data")
        assert parse_args(test_input) == expected


@pytest.mark.parametrize(
    'test_input',
    [
        (['']),
        ([' ']),
        (['r']),
        (['eeee']),
    ]
)
def test_parse_args_raises_exit(test_input):
	try:
		parse_args(test_input)
		assert False
	except SystemExit:
		assert True
