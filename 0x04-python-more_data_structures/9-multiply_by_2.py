#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    k = list(a_dictionary.keys())
    for i in k:
        a_dictionary[i] = a_dictionary[i] * 2
    return a_dictionary
