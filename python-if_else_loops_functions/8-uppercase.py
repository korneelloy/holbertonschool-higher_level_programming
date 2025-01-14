#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            print("{:c}".format(ord(letter) - 32), end='')
        else:
            print("{:c}".format(ord(letter)), end='')
    print('')
