#!/usr/bin/python3

def uppercase(str):
    """This script print a string in uppercase."""
    for each_character in str:
        if 97 <= ord(each_character) <= 122:
            each_character = chr(ord(each_character) - 32)
        print("{}".format(each_character), end="")
    print("")
