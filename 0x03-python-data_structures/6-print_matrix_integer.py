#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for integer in row:
            print("{:d}".format(integer), end="")
            if row[-1] != integer:
                print(" ", end="")
        print()
