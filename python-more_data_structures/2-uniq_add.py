#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_list = set(my_list)
    result = 0
    for element in unique_list:
        result += element
    return result
