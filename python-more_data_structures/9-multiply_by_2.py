#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    updated_dic = {}
    for key, value in a_dictionary.items():
        new = {key: value * 2}
        updated_dic.update(new)
    return updated_dic
