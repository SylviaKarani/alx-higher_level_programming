#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [(my_list[i] if my_list[i] != search else replace)
            for i in range(len(my_list))]
