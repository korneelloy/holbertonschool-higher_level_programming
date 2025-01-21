#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is str:
        return None

    combi = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    result = 0
    last = 0
    roman_string_inverse = roman_string[::-1]

    for el in roman_string_inverse:
        for c in combi.items():
            if c[0] == el:
                if (c[1] >= result or c[1] == last):
                    result += c[1]
                else:
                    result -= c[1]
                last = c[1]
    return (result)
