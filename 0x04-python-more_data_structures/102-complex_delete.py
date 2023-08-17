#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_keys = list(a_dictionary.keys())

    for element_dic in list_keys:
        if value == a_dictionary.get(element_dic):
            del a_dictionary[element_dic]

    return a_dictionary
