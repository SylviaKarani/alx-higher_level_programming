#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    t_sum = 0
    prev = 0

    for i in roman_string[::-1]:
        if i not in values:
            return 0

        if values[i] < prev and prev:
            t_sum -= values[i]
        else:
            t_sum += values[i]

        prev = values[i]

    return t_sum
