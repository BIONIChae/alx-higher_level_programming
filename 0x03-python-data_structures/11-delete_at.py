#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    mod_list = []
    for value in range(len(my_list)):
        if value == idx:
            continue
        mod_list.append(my_list[value])
    my_list.clear()
    my_list.extend(mod_list)
    return mod_list
