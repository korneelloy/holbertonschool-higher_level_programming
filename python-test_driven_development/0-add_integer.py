#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Add 2 integers

    Args:
        a (int): first number / if float, will be transformed to int
        b (int): 2nd number / if float, will be transformed to int

    Returns:
        int: the sum of the 2 numbers

    Raises:
        TypeError if either a or b is not an int nor a float

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
