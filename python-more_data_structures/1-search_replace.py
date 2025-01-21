#!/usr/bin/python3
def search_replace(my_list, search, replace):
    i = 0
    new_list = [0] * len(my_list)
    for element in my_list:
        if element == search:
            new_list[i] = replace
        else:
            new_list[i] = element
        i += 1
    return (new_list)
