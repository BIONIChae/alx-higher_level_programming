#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_list = []
    total = 0
    for num in my_list:
        if num not in n_list:
            n_list.append(num)
            total += num
    return total
