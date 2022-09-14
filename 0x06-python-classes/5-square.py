#!/usr/bin/python3


class Square:
    """Class of Square"""

    def __init__(self, size=0):
        """constructor"""
        if (type(size) is not int):
            raise (TypeError("size must be an integer"))
        elif (size < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = size

    def area(self):
        """get area of the Square"""
        return (self.__size ** 2)

    def my_print(self):
        """print a Square"""
        if (self.__size == 0):
            print()
        else:
            for rows in range(self.__size):
                print("#" * self.__size)

    @property
    def size(self):
        """getter"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """setter"""
        if (type(value) is not int):
            raise (TypeError("size must be an integer"))
        elif (value < 0):
            raise (ValueError("size must be >= 0"))
        else:
            self.__size = value
