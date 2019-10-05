#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for x in range(0, len(matrix)):
        new_matrix.append([])
        for y in range(0, len(matrix)):
            new_matrix[x].append((matrix[x][y] ** 2))

    return new_matrix
