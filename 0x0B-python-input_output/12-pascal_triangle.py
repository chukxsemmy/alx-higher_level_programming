#!/usr/bin/python3

"""Funtion Pascal's Triangle"""


def pascal_triangle(n):
    """define Pascal's Triangle of size n.
    Returns lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pascalTriangle = [[1]]
    while len(pascalTriangle) != n:
        triangle = pascalTriangle[-1]
        tmp = [1]
        for i in range(len(triangle) - 1):
            tmp.append(tri[i] + triangle[i + 1])
        tmp.append(1)
        pascalTriangle.append(tmp)
    return pascalTriangle
