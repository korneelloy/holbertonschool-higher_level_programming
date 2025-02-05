#!/usr/bin/env python3

"""
module for learnig about multiple inheritance
"""


class Fish:
    """fish class"""
    def swim(self):
        """swim method"""
        print("The fish is swimming")

    def habitat(self):
        """habitat method"""
        print("The fish lives in water")


class Bird:
    def fly(self):
        """fly method"""
        print("The bird is flying")

    def habitat(self):
        """habitat method"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    def fly(self):
        """fly method"""
        print("The flying fish is soaring!")

    def swim(self):
        """swim method"""
        print("The flying fish is swimming!")

    def habitat(self):
        """habitat method"""
        print("The flying fish lives both in water and the sky!")


"""test"""

if __name__ == "__main__":
    my_flying_fish = FlyingFish()
    my_flying_fish.fly()
    my_flying_fish.swim()
    my_flying_fish.habitat()
    print(FlyingFish.mro())
