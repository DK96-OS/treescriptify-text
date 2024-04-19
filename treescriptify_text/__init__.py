"""TreeScriptify Package
"""
from .input_data import InputData
from .tree_reader import read_tree_text
from .script_writer import generate_script


def tsfy(data: InputData) -> str:
    """Run Treescriptify on the given Inputs.
    """
    return '\n'.join(
        generate_script(
            read_tree_text(data)
        )
    )
