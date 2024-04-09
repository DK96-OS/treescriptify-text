"""Argument Parsing Methods
"""
from argparse import ArgumentParser
from input.file_validation import validate_input_file

from input.input_data import InputData


def parse_args(arguments: list[str]) -> InputData:
    """Parse the arguments, and determine the program's Input Data.
    """
    try:
        args = _define_arguments().parse_args(arguments)
    except SystemExit as e:
        exit("Unable to Parse Arguments.")
    #
    return InputData(
        tree_text=validate_input_file(args.tree_file_name),
        directories_only=args.directories,
    )


def _define_arguments() -> ArgumentParser:
    """Create and initialize the ArgumentParser.
    """
    parser = ArgumentParser(
        description='Treescriptify Tree Text.'
    )
    parser.add_argument(
        'tree_file_name',
        help='The Tree Text file name.'
    )
    parser.add_argument(
        '-d',
        '--directories',
        action='store_true',
        default=False,
        help='Flag to show only the directories.'
    )
    return parser
