""" Reads the Tree Text and produces Tree Node Data.
"""
from itertools import groupby
from typing import Generator

from treescriptify.tree_node_data import TreeNodeData


def read_tree_text(tree_text: str) -> Generator[TreeNodeData, None, None]:
    """ Read the JSON string and generate TreeNodeData for all elements.
    """
    for line in _split_lines(tree_text):
        if (node := _process_line(line)) is not None:
            yield node


def _split_lines(text: str):
    """ Group characters by whether they're a newline
    """
    for is_newline, chars in groupby(text, key=lambda x: x == '\n'):
        if not is_newline:
            # Join and yield the characters that are not newlines
            yield ''.join(chars)


def _process_line(line: str) -> TreeNodeData | None:
    """ Process the Line Text into a Tree Node Data.
    """
    if line.strip() == "":
        return None
    # Determine the depth by counting the number of spaces or special characters before the name
    depth = (len(line) - len(line.lstrip('│ '))) // 4  # Adjusted based on the given structure

    # Extract the name of the file or directory
    name = line.strip('│ └── ├')

    # Determine if it's a directory
    is_dir = name.endswith('/')

    # If it's a directory, remove the trailing slash
    if is_dir:
        name = name[:-1]
    return TreeNodeData(depth, is_dir, name)
