#!/usr/bin/python3

"""student class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.age = age
        self.last_name = last_name
        self.first_name = first_name

    def to_json(self, attrs=None):
        """transfor class to json for student"""
        if isinstance(attrs, list)\
           and all(isinstance(attr, str) for attr in attrs):
            json_rep = {}
            for key, value in self.__dict__.items():
                for attr in attrs:
                    if key == attr:
                        json_rep[key] = value
            return json_rep
        return {'age': self.age,
                'last_name': self.last_name,
                'first_name': self.first_name}

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        self.age = json['age']
        self.last_name = json['last_name']
        self.first_name = json['first_name']
