#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sol = 0
    i = 0
    while (i < len(roman_string)):
        s1 = num[roman_string[i]]
        if (i + 1 < len(roman_string)):
            s2 = num[roman_string[i + 1]]
            if (s1 >= s2):
                sol = sol + s1
                i = i + 1
            else:
                sol = sol + s2 - s1
                i = i + 2
        else:
            sol = sol + s1
            i = i + 1
    return sol
