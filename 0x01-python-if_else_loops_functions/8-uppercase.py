#!/usr/bin/python3
def uppercase(str):
    up_str = ""
    for val in str:
        if "a" <= val and val <= "z":
            caps = chr(ord(val) - ord("a") + ord("A"))
        else:
            caps = val
        up_str += caps
    print("{:s}".format(up_str), end="")
    print()
