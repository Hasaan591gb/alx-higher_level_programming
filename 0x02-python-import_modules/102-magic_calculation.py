#!/usr/bin/python3
def my_function(a, b):
    from magic_calculation_102 import add as add, sub as sub
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        return sub(a, b)
