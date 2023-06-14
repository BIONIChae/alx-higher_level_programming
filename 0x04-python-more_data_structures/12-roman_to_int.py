#!/usr/bin/python3
def roman_to_int(roman_string):
    l = {'I': 1, 'V' : 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = 0
    for i in roman_string:
        if i in l:
            integer += l[i]
    return integer
