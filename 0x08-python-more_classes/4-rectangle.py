#!/usr/bin/python3
""" This is a rectangle module
"""


class Rectangle:
    """This is a Rectangle class with a getter and setter for the width
    """

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        add = self.__width + self.__height
        return add * 2

    def __str__(self):
        if self.__width == 0 and self.__height == 0:
            return ""
        result = ""
        for i in range(self.__height):
            for j in range(self.__width):
                result += "#"
            result += "\n"
        return result

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
