#!/usr/bin/python3
"""
This module has a function that adds two
integer numbers and returns the result.

"""
def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a: First integer.
        b: Second integer.
    Return:
        The addition of the two numbers.
        If the function receive a parameter
        that is not a integer raise a TypeError
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
