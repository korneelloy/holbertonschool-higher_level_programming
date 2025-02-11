#!/usr/bin/python3

"""student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """transfor class to json for student"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}
