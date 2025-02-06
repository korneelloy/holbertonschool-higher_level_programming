#!/usr/bin/env python3

"""
module for learnig method overriding
"""


class CountedIterator:
    """
    class adding counting to iterator
    """
    def __init__(self, some_iterable):
        """
        init method
        """
        self.some_iterable = some_iterable
        self.iterator = iter(some_iterable)
        self.counter = 0

    def get_count(self):
        """
        count nb of itterations
        """
        return self.counter

    def __next__(self):
        """
        overwrite the next function of iter
        """
        try:
            value = next(self.iterator)
            self.counter += 1
            return value
        except StopIteration:
            raise StopIteration


""" testing """
if __name__ == "__main__":
    data = [1, 2, 3, 4]
    counted_iter = CountedIterator(data)

    try:
        while True:
            item = next(counted_iter)
            print(f"Got {item}, total {counted_iter.get_count()} items iterd")
    except StopIteration:
        print("No more items.")
