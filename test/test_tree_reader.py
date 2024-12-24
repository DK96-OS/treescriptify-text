""" Testing Tree Reader Methods.
"""
from treescriptify_text.tree_node_data import TreeNodeData
from treescriptify_text.tree_reader import read_tree_text


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
    assert not result[0].is_dir


def test_read_tree_text_single_dir_returns_single_data():
    text = 'my-app/'
    result = list(read_tree_text(text))
    assert len(result) == 1
    assert result[0].name == 'my-app'
    assert result[0].depth == 0
    assert result[0].is_dir


def test_read_tree_text_basic_tree_returns_data():
    text = '''
test
├── __init__.py
├── input
│   ├── test_argument_parser.py
└── treescriptify
    └── test_tree_reader.py
    '''
    result = list(read_tree_text(text))
    assert len(result) == 6
    assert result == [
        TreeNodeData(0, True, 'test'),
        TreeNodeData(1, False, '__init__.py'),
        TreeNodeData(1, True, 'input'),
        TreeNodeData(2, False, 'test_argument_parser.py'),
        TreeNodeData(1, True, 'treescriptify'),
        TreeNodeData(2, False, 'test_tree_reader.py'),
    ]


def test_read_tree_text_complex_tree1_returns_data():
    text = '''
test
├── __init__.py
├── input
│   ├── __init__.py
│   ├── test_argument_parser.py
│   ├── test_file_validation.py
│   └── test_string_validation.py
└── treescriptify
    ├── test_script_writer.py
    └── test_tree_reader.py
    '''
    result = list(read_tree_text(text))
    assert len(result) == 10
    assert result == [
        TreeNodeData(0, True, 'test'),
        TreeNodeData(1, False, '__init__.py'),
        TreeNodeData(1, True, 'input'),
        TreeNodeData(2, False, '__init__.py'),
        TreeNodeData(2, False, 'test_argument_parser.py'),
        TreeNodeData(2, False, 'test_file_validation.py'),
        TreeNodeData(2, False, 'test_string_validation.py'),
        TreeNodeData(1, True, 'treescriptify'),
        TreeNodeData(2, False, 'test_script_writer.py'),
        TreeNodeData(2, False, 'test_tree_reader.py'),
    ]


def test_read_tree_text_complex_tree2_returns_data():
    text = '''com
└── yourapp
    ├── ui
    │   ├── theme
    │   │   ├── Color.kt
    │   │   ├── Shape.kt
    │   │   ├── Theme.kt
    │   │   └── Type.kt
    │   │
    │   ├── atoms
    │   │   ├── ButtonPrimary.kt
    │   │   ├── ButtonSecondary.kt
    │   │   ├── IconLoader.kt
    │   │   ├── TextInputField.kt
    │   │   ├── ToggleSwitch.kt
    │   │   └── TypographyText.kt
    │   │
    │   └── pages
    │       ├── LoginPage.kt
    │       ├── UserProfilePage.kt
    │       ├── ArticleListPage.kt
    │       └── ProductCatalogPage.kt
    │
    └── utils
        └── Extensions.kt
    '''
    result = list(read_tree_text(text))
    assert len(result) == 22
    assert result == [
        TreeNodeData(0, True, 'com'),
        TreeNodeData(1, True, 'yourapp'),
        TreeNodeData(2, True, 'ui'),
        TreeNodeData(3, True, 'theme'),
        TreeNodeData(4, False, 'Color.kt'),
        TreeNodeData(4, False, 'Shape.kt'),
        TreeNodeData(4, False, 'Theme.kt'),
        TreeNodeData(4, False, 'Type.kt'),
        TreeNodeData(3, True, 'atoms'),
        TreeNodeData(4, False, 'ButtonPrimary.kt'),
        TreeNodeData(4, False, 'ButtonSecondary.kt'),
        TreeNodeData(4, False, 'IconLoader.kt'),
        TreeNodeData(4, False, 'TextInputField.kt'),
        TreeNodeData(4, False, 'ToggleSwitch.kt'),
        TreeNodeData(4, False, 'TypographyText.kt'),
        TreeNodeData(3, True, 'pages'),
        TreeNodeData(4, False, 'LoginPage.kt'),
        TreeNodeData(4, False, 'UserProfilePage.kt'),
        TreeNodeData(4, False, 'ArticleListPage.kt'),
        TreeNodeData(4, False, 'ProductCatalogPage.kt'),
        TreeNodeData(2, True, 'utils'),
        TreeNodeData(3, False, 'Extensions.kt'),
    ]


def test_read_tree_text_issue_9_returns_data():
    text = '''poetry-demo
├── pyproject.toml
├── README.md
├── poetry_demo
│   └── __init__.py
└── tests
    └── __init__.py'''
    result = list(read_tree_text(text))
    print(result)
    assert len(result) == 7
    assert result == [
        TreeNodeData(0, True, 'poetry-demo'),
        TreeNodeData(1, False, 'pyproject.toml'),
        TreeNodeData(1, False, 'README.md'),
        TreeNodeData(1, True, 'poetry_demo'),
        TreeNodeData(2, False, '__init__.py'),
        TreeNodeData(1, True, 'tests'),
        TreeNodeData(2, False, '__init__.py'),
    ]
