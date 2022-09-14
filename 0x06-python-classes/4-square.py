#!/usr/bin/python3
"""
module with Class
"""


class Square:
    """a square class"""
    def __init__(self, size=0):
        """constructor"""
        self.__size = size

    def area(self):
        """area of Square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
