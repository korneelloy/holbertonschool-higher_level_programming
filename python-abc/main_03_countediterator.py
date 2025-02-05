#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

while True:
    item = next(counted_iter)
    print(f"Got {item}, total {counted_iter.get_count()} items iterated.")

