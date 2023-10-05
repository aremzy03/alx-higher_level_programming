#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = sys.argv
sum = 0
for num in argv:
    if num == argv[0]:
        continue
    num = int(num)
    sum += num
print(sum)
