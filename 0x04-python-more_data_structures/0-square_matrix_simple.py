#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    ret = []
    for i in range(len(matrix)):
        ret.append(list(map(lambda x: x ** 2, matrix[i])))

    return ret
