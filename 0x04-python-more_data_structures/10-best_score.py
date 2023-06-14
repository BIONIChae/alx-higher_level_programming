#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return
    biggest_score = 0
    name = None
    for key, val in a_dictionary.items():
        if val > biggest_score:
            biggest_score = val
            name = key
    return name
