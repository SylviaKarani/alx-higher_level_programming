#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best = None
    for i in a_dictionary:
        best = i if best is None else best
        if a_dictionary[i] > a_dictionary[best]:
            best = i

    return best
