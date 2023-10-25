#!/usr/bin/python3
class Square:
    """This a square class that does alot
    """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        return self._Square__size ** 2
