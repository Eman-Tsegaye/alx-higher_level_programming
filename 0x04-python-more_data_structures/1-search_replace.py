#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    n = len(new)
    for i in range(0, n):
        if new[i] == search:
            new[i] = replace
    return new
