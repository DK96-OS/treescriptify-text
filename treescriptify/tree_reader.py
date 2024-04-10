""" Reads the Tree Text and produces Tree Node Data.
"""
from itertools import groupby
from typing import Generator

from treescriptify.tree_node_data import TreeNodeData


def read_tree_text(tree_text: str) -> Generator[TreeNodeData, None, None]:
    """ Read the Tree Text string and generate TreeNodeData for all elements.
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
    # Extract the name of the file or directory
    if (name := line.strip('│ └── ├\xa0')) == "":
        return None # Ignore Empty Lines
    if name.startswith('#') or name.startswith('//'):
        return None # Ignore comments
    # Determine directory status
    if name.endswith('/'):
        is_dir = True
        name = name[:-1] # If it's a directory, remove the trailing slash
    elif name.startswith('.'):
        # hidden file or dir
        simple_name = name.lstrip('.')
        # check for presence of file extension
        is_dir = '.' not in simple_name
    elif '.' not in name:
        # no file extension
        is_dir = True
    else:
        is_dir = False
    return TreeNodeData(_calculate_depth(line), is_dir, name)


def _calculate_depth(line: str) -> int:
    """Calculate the Depth of a Line in the Tree.
    """
    if '──' not in line:
        return 0
    # Use Length of Indentation
    if (i_length := len(line.split('──')[0])) == 0:
        return 0
    return (i_length + 3) // 4
