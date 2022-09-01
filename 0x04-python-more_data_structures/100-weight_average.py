#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    val1 = 0
    val2 = 0

    for vals in my_list:
        val1 += vals[0] * vals[1]
        val2 += vals[1]
    weighted_avg = val1 / val2
    return (weighted_avg)
