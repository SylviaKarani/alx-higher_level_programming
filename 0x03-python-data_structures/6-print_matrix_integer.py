#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        k = 0
        for j in range(len(i)):
            print("{:d}".format(i[j]), end=" " if j < len(i) - 1 else "\n")
            k += 1

    if len(matrix[0]) == 0:
        print("{}".format(""))
