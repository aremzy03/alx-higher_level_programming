#!/usr/bin/python3
"""
this is a program that adds integers
"""


def add_integer(a, b=98):
    """Returns the sum of the integers

    Args:
        a (_type_): the first arguement
        b (int, optional): the second argument. Defaults to 98.

    Returns:
        an int: the sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    result = a + b
    if isinstance(result, float):
        fresult = round(result, 2)
        return fresult
    return result
