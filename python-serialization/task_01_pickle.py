#!/usr/bin/env python3

"""pickle module"""

import pickle


class CustomObject:
    """an object"""
    def __init__(self, name, age, is_student):
        """init method"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """print function"""
        print("Name: {}\nAge: {}\nIs Student: {}"
              .format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        serialize current instance of object via pickle module
        and save to filename
        argv:
            filename
        """
        if not filename:
            return None
        if not isinstance(self, CustomObject):
            return None
        else:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        load and return an instance of the CustomObjec using Pickle module
        argv:
            filename
        """
        with open(filename, 'rb') as file:
            if not filename:
                return None
            deserialized_file = pickle.load(file)
            if not isinstance(deserialized_file, CustomObject):
                return None
            else:
                return deserialized_file
