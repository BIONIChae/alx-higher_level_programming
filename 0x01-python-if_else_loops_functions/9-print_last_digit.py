#!/usr/bin/python3
def print_last_digit(number):
    end_num = abs(number) % 10
    print(end_num, end="")
    return end_num
