"""TreeScriptify Package
"""
from input.input_data import InputData
from treescriptify.tree_reader import read_tree_text
from treescriptify.script_writer import generate_script


def tsfy(data: InputData) -> str:
    """Run Treescriptify on the given Inputs.
    """
    return '\n'.join(
        generate_script(
            read_tree_text(data)
        )
    )
