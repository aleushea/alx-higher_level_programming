#!/usr/bin/python3
# This script is task three-print_reversed_list_integer.py


def print_reversed_list_integer(my_list=[]):
    """Print all integers of a list in reverse order."""
    if my_list:
        my_list.reverse()
        for item in range(len(my_list)):
            print("{:d}".format(my_list[item]))
