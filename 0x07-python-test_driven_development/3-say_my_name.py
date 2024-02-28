#!/usr/bin/python3
"""Say my name file with a function that prints a  name"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
