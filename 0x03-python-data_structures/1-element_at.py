#!/usr/bin/python3
def element_at(my_list, idx):
    largo = len(my_list)
    if idx > largo:
        return (None)
    elif idx < 0:
        return (None)
    else:
        return my_list[idx]
