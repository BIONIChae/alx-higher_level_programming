#!/usr/bin/python3
def search_replace(my_list, search, replace):
    n_list = list(map(lambda n: replace if n == search else n, my_list))
    return n_list
