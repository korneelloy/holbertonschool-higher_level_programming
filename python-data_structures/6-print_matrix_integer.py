#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sublist in matrix:
        for el in sublist:
            print("{:d}".format(el), end=' ')
        print("".format())
