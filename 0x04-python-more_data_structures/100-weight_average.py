#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for each_weight in my_list:
        numerator += each_weight[0] * each_weight[1]
        denominator += each_weight[1]

    return numerator / denominator
