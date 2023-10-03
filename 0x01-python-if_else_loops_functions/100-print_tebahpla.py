#!/usr/bin/python3
check = 1
for i in range(ord('z'), ord('a') - 1, -1):
    check += 1
    if check % 2 != 0:
        i -= 32
    print(chr(i), end="")
