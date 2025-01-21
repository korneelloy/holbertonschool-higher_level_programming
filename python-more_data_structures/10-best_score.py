#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = (list(a_dictionary.values())[0])
        index = 0
        for i in range(1, len(a_dictionary)):
            if (list(a_dictionary.values())[i] > max):
                max = list(a_dictionary.values())[i]
                index = i
        return list(a_dictionary.keys())[index]
    else:
        return None
