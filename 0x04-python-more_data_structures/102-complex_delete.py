#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = list(a_dictionary.keys())
    for index in k:
        if a_dictionary[index] == value:
            del a_dictionary[index]
    return a_dictionary
