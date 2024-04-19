"""String Validation Methods.
"""


def validate_name(argument) -> bool:
    """
    Determine whether an argument is a non-empty string.
        Does not count whitespace.
        Uses the strip method to remove empty space.

    Parameters:
    - argument (str) : The given argument.

    Returns:
    bool - True if the argument qualifies as valid.
    """
    if argument is None or not isinstance(argument, str):
        return False
    elif len(argument.strip()) < 1:
        return False
    return True
