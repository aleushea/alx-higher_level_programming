#!/usr/bin/python3
"""
The lookup function container
"""


def lookup(obj):
    """
    Args:the function named lookup(obj) takes a single parameter obj
    obj: initial object
    Returns: return a list of attributes and methods associated with the object
    """
    return dir(obj)
