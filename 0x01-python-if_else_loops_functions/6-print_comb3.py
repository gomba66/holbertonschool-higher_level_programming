#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        if num2 > num1 and num1 != 8:
            print("{}{}, ".format(num1, num2), end="")
        elif num2 > num1 and num1 == 8:
            print("{}{}".format(num1, num2))
