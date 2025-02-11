#!/usr/bin/python3

class Student:
    def __init__(self, first_name, last_name, age):
        self.f_n = first_name
        self.l_n = last_name
        self.age = age

    def to_json(self):
        return {'first_name': self.f_n, 'last_name': self.l_n, 'age': self.age}
