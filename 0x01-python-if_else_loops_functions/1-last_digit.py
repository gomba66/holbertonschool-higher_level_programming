#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of", number, end=" ")
if number > 0:
    number = number % 10
else:
    number = number % -10

if number == 0:
    print("is", number, "and is 0")
elif number < 0:
    print("is", number, "and is less than 6 and not 0")
else:
    print("is", number, "and is less than 6 and not 0")
