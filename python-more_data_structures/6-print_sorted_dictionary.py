#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for cle, valeur in sorted(a_dictionary.items()):
        print(f"{cle}: {valeur}")
