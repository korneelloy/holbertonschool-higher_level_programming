#!/usr/bin/env python3

"""
module for learnig about mixin
"""


class SwimMixin:
    """ex of mixin class"""
    def swim(self, message):
        """swim method"""
        print(message)


class FlyMixin:
    """ex of mixin class"""
    def fly(self, message):
        """fly method"""
        print(message)


class Dragon(SwimMixin, FlyMixin):
    """dragon class"""
    def roar(self):
        """roar method"""
        print("The dragon roars!")

    def swim(self):
        """swim method"""
        super().swim("The creature swims!")

    def fly(self):
        """fly methox"""
        super().fly("The creature flies!")


"""test"""

if __name__ == "__main__":
    draco = Dragon()
    draco.swim()
    draco.fly()
    draco.roar()
