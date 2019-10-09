#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = []
    for x in matrix:
        ele = list(map((lambda x: x ** 2), x))
        new_matrix.append(ele)
    return new_matrix
