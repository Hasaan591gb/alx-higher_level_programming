#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_list = [0, 0]
    for i in range(len(tuple_a)):
        if i == 2:
            break
        my_list[i] += tuple_a[i]
    for j in range(len(tuple_b)):
        if j == 2:
            break
        my_list[j] += tuple_b[j]
    return my_list[0], my_list[1]
