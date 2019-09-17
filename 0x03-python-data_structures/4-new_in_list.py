#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copylist = []
    x = 0
    for i in my_list:
        x = x + 1
        copylist.append(i)
    if idx < 0:
        return copylist
    elif idx > len(my_list):
        return copylist
    else:
        copylist[idx] = element
        return copylist
