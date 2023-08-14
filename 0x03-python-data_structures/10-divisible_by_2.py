#!/usr/bin/python3
# question number 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """this function finds all multiples of 2 in a list."""
    new_list = []
    for index_of_num in range(len(my_list)):
        if my_list[index_of_num] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
