#!/usr/bin/env python3

"""
module for learnig method overriding
"""


class VerboseList(list):
    """
    class adding some print functionality to std list mrthods
    """
    def append(self, item):
        """
        add print message to list appending
        """
        print(f"Added [{item}] to the list.")
        super().append(item)

    def extend(self, items):
        """
        add print message to list extending
        """
        print(f"Extended the list with [{len(items)}] items.")
        super().extend(items)

    def remove(self, item):
        """
        add print message to list removal
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, position=-1):
        """
        add print message to list popping
        """
        print(f"Popped [{self[position]}] from the list.")
        super().pop(position)


v_list = VerboseList([1, 2, 3, 4, 4])
print(v_list)
v_list.append(4)
v_list.append(8)
v_list.extend([5, 6, 7])
v_list.remove(4)
v_list.pop()
v_list.pop(2)
print(v_list)
try:
    v_list.pop(15)
except IndexError:
    print("IndexError exception called")

try:
    v_list.remove(10)
except ValueError:
    print("ValueError exception called")

try:
    v_list.append()
except TypeError:
    print("TypeError exception called")

try:
    v_list.extend(5)
except TypeError:
    print("TypeError exception called")
