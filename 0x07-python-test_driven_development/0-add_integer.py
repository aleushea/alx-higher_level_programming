#!/usr/bin/python3
"""the purpose of this module is addition of two integers/floating point mumbers"""


def add_integer(a, b=98):
    """
    this function adds two  integers/floating point numbers a and b
    Raise TypeError if a or b are not integers/floating points numbers
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("the variable a must be an integer/floating number")

    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("the variable b must be an integer/floating number")

    a = int(a)
    b = int(b)

    return a + b
