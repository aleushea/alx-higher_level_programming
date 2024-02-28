#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):
    """Find the largest integer of a list."""
    if len(my_list) == 0:
        return None

    biggest = my_list[0]
    for index in range(len(my_list)):
        if my_list[index] > biggest:
            biggest = my_list[index]

    return biggest
