#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a += (0, 0)
    if len(tuple_b) < 2:
        tuple_b += (0, 0)
    a_one, a_two = tuple_a[:2]
    b_one, b_two = tuple_b[:2]
    new_tuple = (a_one + b_one, a_two + b_two)
    return new_tuple
