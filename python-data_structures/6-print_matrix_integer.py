#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix[0]) == 0:
        print("")
    for sublist in matrix:
        for i in range(len(sublist)):
            if (i == len(sublist) - 1):
                print("{:d}".format(sublist[i]))
            else:
                print("{:d}".format(sublist[i]), end=" ")
