#!/usr/bin/python3
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif b < c:
        return b + a
    else:
        return (a * b) - c
