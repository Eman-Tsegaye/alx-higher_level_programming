#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
if number < 0:
    last *= -1
if last == 0:
    cmp = "0"
elif last <= 5:
    cmp = "less than 6 and not 0"
else:
    cmp = "greater than 5"
print(f"Last digit of {number:d} is {last:d} and is {cmp}")
