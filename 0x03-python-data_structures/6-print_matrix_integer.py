#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 1:
        print([])
    else:
        i = 0
        j = 0
        while i < len(matrix):
            j = 0
            while j < len(matrix):
                if j == len(matrix) - 1:
                    print("{}".format(matrix[i][j]), end='')
                else:
                    print("{}".format(matrix[i][j]), end=' ')
                j = j + 1
            print()
            i = i + 1
