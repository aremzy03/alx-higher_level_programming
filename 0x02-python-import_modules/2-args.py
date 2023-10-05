#!/usr/bin/python3
import sys
if __name__ == "__main__":
	argv = sys.argv
length = len(argv) - 1
if length < 1:
    print(f"{length} arguments.")
elif length == 1:
    print(f"{length} argument:")
else:
    print(f"{length} arguments:")
count = 1
for argument in argv:
    if argument == argv[0]:
        continue
    print("{}: {}".format(count, argument))
    count += 1
