#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for x in range(0, len(matrix)):
        new.append(['0']*len(matrix))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            new[i][j] = matrix[i][j] ** 2
    return new
