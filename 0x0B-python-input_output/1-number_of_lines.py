#!/usr/bin/python3
def number_of_lines(filename=""):
    x = 0
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            x += 1
        return x
