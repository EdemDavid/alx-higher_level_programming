#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lasdig = abs(number) % 10

if lasdig > 5:
    print(f"Last digit of {number:d} is {lasdig:d} and is greater than 5")
elif lasdig == 0:
    print(f"Last digit of {number:d} is {lasdig:d} and is 0")
else:
    print(f"Last digit of {number:d} is {lasdig:d} and is less than 6 and not 0")
