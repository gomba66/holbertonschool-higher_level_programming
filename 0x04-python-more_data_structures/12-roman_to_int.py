#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or roman_string is not str:
        return 0
    M, D, C, L, X, V, I = 1000, 500, 100, 50, 10, 5, 1
    total2 = 0
    new_list = []
    for i in range(len(roman_string)):
        if roman_string[i] == 'M':
            new_list.append(M)
        elif roman_string[i] == 'D':
            new_list.append(D)
        elif roman_string[i] == 'C':
            new_list.append(C)
        elif roman_string[i] == 'L':
            new_list.append(L)
        elif roman_string[i] == 'X':
            new_list.append(X)
        elif roman_string[i] == 'V':
            new_list.append(V)
        elif roman_string[i] == 'I':
            new_list.append(I)
    new_list.append(0)
    new_list.insert(0, 0)
    for idx in range(len(new_list)):
        if idx < len(new_list) - 1:
            if new_list[idx] >= new_list[idx + 1]:
                total2 = total2 + new_list[idx]
            if new_list[idx] < new_list[idx + 1]:
                total2 = total2 - new_list[idx]
    return total2
