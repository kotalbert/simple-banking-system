"""Utilities module for the Simple Banking System."""


def digits_to_string(digits: list[int]) -> str:
    """Convert a list of integers representing digits to a string.

    :param digits: A list of integers.
    :return: A string representation of the digits.
    """

    return ''.join(map(str, digits))
