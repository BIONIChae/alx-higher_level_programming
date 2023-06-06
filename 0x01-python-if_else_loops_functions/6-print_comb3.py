#!/usr/bin/python3
for num in range(0, 10):
    for dig in range(0, 10):
        if num < dig:
            if (num == 8) and( dig == 9):
                print(f"{num:d}{dig:d}")
            else:
                print(f"{num:d}{dig:d}", end=', ')
