#!/usr/bin/python3

"""Pascal s Triangle"""


def pascal_triangle(n):
    """ returns a list of lists of integers
    representing the Pascal s triangle"""
    the_list = []
    prev_sublist = []
    next_sublist = []
    if n <= 0:
        return the_list
    else:
        next_sublist = [1]
        the_list.append(next_sublist)
        if n == 1:
            return the_list
        else:
            prev_sublist = [1, 1]
            the_list.append(prev_sublist)
            if n == 2:
                return the_list
            else:
                for times in range(n-2):
                    next_sublist = []
                    next_sublist.insert(0, 1)
                    for index in range(1, times+2):
                        value = prev_sublist[index] + prev_sublist[index-1]
                        next_sublist.insert(index, value)
                    the_list.append(next_sublist)
                    next_sublist.insert(n, 1)
                    prev_sublist = next_sublist.copy()

                return the_list
