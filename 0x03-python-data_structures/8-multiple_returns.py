#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
    length = 0
    for char in sentence:
        length += 1
    return length, sentence[0]
