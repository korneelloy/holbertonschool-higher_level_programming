#!/usr/bin/env python3

"""
module for learnig abstract classes
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    abstract animal class
    """
    @abstractmethod
    def sound(self):
        """
        abstract sound method
        """
        pass


class Dog(Animal):
    """
    dog class
    """
    def sound(self):
        """
        implementation of sound method for dog
        """
        return "Bark"


class Cat(Animal):
    """
    cat class
    """
    def sound(self):
        """
        implementation of sound method for cat
        """
        return "Meow"
