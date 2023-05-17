#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_score = sum(item[0] * item[1] for item in my_list)
    total_weight = sum(item[1] for item in my_list)
    return total_score / total_weight
