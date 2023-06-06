#!/usr/bin/python3
for lower_ascii in range(97, 123):
    if (chr(lower_ascii) == 'q' or chr(lower_ascii) == 'e'):
        continue
    print(chr(lower_ascii).format(), end='')
