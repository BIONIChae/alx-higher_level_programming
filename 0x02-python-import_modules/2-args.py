#!/usr/bin/python3
import sys

argv = sys.argv[1:]
len_of_arguments = len(argv)
if len_of_arguments == 0:
    print(f"{len_of_arguments} arguments.")
elif len_of_arguments == 1:
    print(f"{len_of_arguments} argument:\n{len_of_arguments}: {argv[0]}")
else:
    print(f"{len_of_arguments} arguments:")
    for index in range(len(argv)):
        print(f"{index + 1}: {argv[index]}")

if __name__ == '__main__':
    pass
