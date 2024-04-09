"""Input Data to the Program
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class InputData:
    """The Input tree data and optional flags to modify the output of the program.
    """

    tree_text: str
    #
    directories_only: bool = False
