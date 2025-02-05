#!/usr/bin/env python3

"""
module for learnig method overriding
"""
class VerboseList(list):
    def append(self):
        super().append()
        print("xxxx")
    def extend(self):
        pass
    def remove(self):
        pass
    def pop(self):
        pass