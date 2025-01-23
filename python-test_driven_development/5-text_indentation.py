#!/usr/bin/python3

"""
The text_indentation module handles
printing 2 new lines after special characters

This is handled through the text_indentation function
"""


def text_indentation(text):
    """
    Prints 2 new lines after special characters . ? :
    Args:
        text: a string
    Returns:
        None
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for letter in text:
        if letter in ('.', '?', ':'):
            line = line + letter
            line = line.strip()
            print("{:s}".format(line))
            print()
            line = ""
        else:
            line = line + letter
    if letter not in ('.', '?', ':'):
        line = line.strip()
        print("{:s}".format(line), end='')
