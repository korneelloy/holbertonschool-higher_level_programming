#!/usr/bin/python3

"""
The print_square module prints a square of # of given size

This is handled through the print_square function
"""


def print_square(size):
    """
    prints a square of # of given size
    Args:
        size: number of rows / columns
    Returns:
        None
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for times in range(size):
        print("#" * size)
