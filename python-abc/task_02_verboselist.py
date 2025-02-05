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
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        add print message to list extending
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        add print message to list removal
        """
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, position=-1):
        """
        add print message to list popping
        """
        popped = super().pop(position)
        print(f"Popped [{popped}] from the list.")


v_list = VerboseList([1, 2, 3, 4, 4])
print(v_list)
v_list.append(4)
v_list.append(8)
v_list.extend([5, 6, 7])
v_list.remove(4)
v_list.pop()
v_list.pop(2)
print(v_list)
v_list.pop(15)
v_list.remove(9)
