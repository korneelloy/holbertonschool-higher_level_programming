#!/usr/bin/python3

"""
The 0-add_integer module handles adding and returning 2 numbers
This is handled through the add_integer function
"""


def add_integer(a, b=98):
    """
    Add 2 integers
    Args:
        a (int): first number / if float, will be transformed to int
        b (int): 2nd number / if float, will be transformed to int
    Returns:
        int: the sum of the 2 numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
