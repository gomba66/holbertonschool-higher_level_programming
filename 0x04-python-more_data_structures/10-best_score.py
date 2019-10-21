#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    k = list(a_dictionary.keys())
    for i in k:
        if a_dictionary[i] >= max(list(a_dictionary.values())):
            maxi_k = i
    return maxi_k
