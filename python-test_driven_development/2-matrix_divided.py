#!/usr/bin/python3

"""
The 2-matrix_divided module handles dividing a matrix
(list of lists of integers) by a given number
This is handled through the matrix_divided function
"""


def matrix_divided(matrix, div):
    """
    Dividing a matrix (list of lists of integers) by a given number
    Args:
        matrix: list of lists of integers
        div (int): the devider
    Returns:
        new matrix of divided numbers
    """
    lenght = -1
    for line in matrix:
        if lenght == -1:
            lenght = len(line)
        else:
            if lenght != len(line):
                message = "Each row of the matrix must have the same size"
                raise TypeError(message)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    message = "matrix must be a matrix (list of lists) of integers/floats"
    for line in matrix:
        try:
            new_line = [round(x / div, 2) for x in line]
        except TypeError:
            raise TypeError(message)
        else:
            new_matrix.append(new_line)
    return new_matrix
