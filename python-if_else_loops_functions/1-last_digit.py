#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last = 0 - last
phrase = "Last digit of " + str(number) + " is " + str(last) + " and is"
if last > 5:
    print(f"{phrase} greater than 5")
elif last == 0:
    print(f"{phrase} 0")
else:
    print(f"{phrase} less than 6 and not 0")
