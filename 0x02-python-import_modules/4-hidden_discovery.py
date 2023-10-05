#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    name = dir(hidden_4)
    for i in sorted(name):
        if i.startswith("__"):
            continue
        else:
            print(i)
