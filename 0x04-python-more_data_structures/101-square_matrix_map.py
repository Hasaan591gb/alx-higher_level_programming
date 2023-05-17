#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda my_list:
                list(map(lambda x: x ** 2, my_list)), matrix))
