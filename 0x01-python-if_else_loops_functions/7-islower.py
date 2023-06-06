#!/usr/bin/python3
def islower(c):
    for int in range(97, 123):
        lower_list = list(chr(int))
        if c in lower_list:
            return True
        else:
            return False
