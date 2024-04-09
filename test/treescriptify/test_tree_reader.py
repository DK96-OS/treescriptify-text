""" Testing Tree Reader Methods.
"""
from treescriptify.tree_reader import read_tree_text


def test_read_tree_text_empty_text_returns_empty_list():
    text = ''
    result = list(read_tree_text(text))
    assert len(result) == 0


def test_read_tree_text_blank_text_returns_empty_list():
    text = ' '
    result = list(read_tree_text(text))
    assert len(result) == 0


def test_read_tree_text_single_file_returns_single_data():
    text = 'file.txt'
    result = list(read_tree_text(text))
    assert len(result) == 1
    assert result[0].name == 'file.txt'
    assert result[0].depth == 0
    assert result[0].is_dir == False


def test_read_tree_text_single_dir_returns_single_data():
    text = 'my-app/'
    result = list(read_tree_text(text))
    assert len(result) == 1
    assert result[0].name == 'my-app'
    assert result[0].depth == 0
    assert result[0].is_dir == True
