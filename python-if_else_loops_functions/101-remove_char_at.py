#!/usr/bin/python3
def remove_char_at(str, n):
    index = 0
    copy = ""
    for c in str:
        if n != index:
            copy = copy + c
        index = index + 1
    return (copy)
