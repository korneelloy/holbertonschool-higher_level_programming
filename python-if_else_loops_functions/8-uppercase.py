#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            ord_letter = ord(letter) - 32
        else:
            ord_letter = ord(letter)
        print("{:c}".format(ord_letter), end='')
    print('')
