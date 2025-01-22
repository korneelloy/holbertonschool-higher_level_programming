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
    message_1 = "matrix must be a matrix (list of lists) of integers/floats"
    message_2 = "Each row of the matrix must have the same size"
    message_3 = "div must be a number"
    message_4 = "division by zero"
    lenght = -1
    for line in matrix:
        if lenght == -1:
            try:
                lenght = len(line)
            except TypeError:
                raise TypeError(message_1)
        else:
            if lenght != len(line):
                raise TypeError(message_2)
    if not isinstance(div, (int, float)):
        raise TypeError(message_3)
    if div == 0:
        raise ZeroDivisionError(message_4)
    new_matrix = []
    for line in matrix:
        try:
            new_line = [round(x / div, 2) for x in line]
        except TypeError:
            raise TypeError(message_1)
        else:
            new_matrix.append(new_line)
    return new_matrix
