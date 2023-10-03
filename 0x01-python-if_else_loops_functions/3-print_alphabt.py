#!/usr/bin/python3
for ascii_val in range(ord('a'), ord('z') + 1):
    if ascii_val == 101 or ascii_val == 113:
        continue
    print(chr(ascii_val), end="")
