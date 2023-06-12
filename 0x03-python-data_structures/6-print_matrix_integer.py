#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for column in range(len(r)):
            if column == len(r) - 1:
                print("{:d}".format(r[column]), end="")
            else:
                print("{:d}".format(r[column]), end=" ")
        print()
