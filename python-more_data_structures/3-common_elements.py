#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_list = []
    for element_1 in set_1:
        for element_2 in set_2:
            if element_1 == element_2:
                new_list.append(element_1)
    return new_list
