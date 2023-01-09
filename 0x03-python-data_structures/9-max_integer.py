#!/usr/bin/python3
def max_integer(my_list=[]):
    l_max = my_list[0] if len(my_list) else None
    for i in my_list:
        if i > l_max:
            l_max = i

    return l_max
