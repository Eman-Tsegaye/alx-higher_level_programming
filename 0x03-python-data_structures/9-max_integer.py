#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None
    bigger = my_list[0]
    for i in my_list:
        if i > bigger:
            bigger = i
    return(bigger)
