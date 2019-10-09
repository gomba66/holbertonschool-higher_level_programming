#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    res = 0
    new_list = list(set(my_list))
    for index in new_list:
        res = res + index
    return res
