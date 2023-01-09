#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    a_dictionary.update({key: value})

    return a_dictionary
