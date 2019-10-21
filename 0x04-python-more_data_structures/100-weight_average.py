#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        score, weight = 0, 0
        for i in range(len(my_list)):
                score = score + my_list[i][0] * my_list[i][1]
                weight = weight + my_list[i][1]
        average = score / weight
    return average
