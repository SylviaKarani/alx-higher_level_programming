#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    wxs = 0
    w = 0
    for i in my_list:
        wxs += (i[0] * i[1])
        w += i[1]
    return wxs / w
