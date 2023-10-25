#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self._Square__size = size
        self._Square__pos = position

    @property
    def size(self):
        return self._Square__size

    def position(self):
        return self._Square__pos
        
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__pos = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        for i in range(self._Square__size):
            for k in range(self._Square__pos[0]):
                print(" ",end="")
            for j in range(self._Square__size):
                print("#", end="")
            print("")
