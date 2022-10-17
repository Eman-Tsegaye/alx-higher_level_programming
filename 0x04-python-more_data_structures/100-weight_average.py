#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    ful_sum = 0
    sum = 0
    for i, j in my_list:
        sum += j
        ful_sum += i * j
    return ful_sum / sum
