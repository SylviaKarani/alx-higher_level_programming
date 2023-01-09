#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return

    x = list(a_dictionary.keys())
    x.sort()
    for i in x:
        print(f"{i:s}: {a_dictionary[i]}")
