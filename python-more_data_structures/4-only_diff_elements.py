#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = list(set_1) + list(set_2)
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] == new_list[j]:
                new_list.remove(new_list[i])
                new_list.remove(new_list[j - 1])
                break
    new_set = set(new_list)
    return new_set
