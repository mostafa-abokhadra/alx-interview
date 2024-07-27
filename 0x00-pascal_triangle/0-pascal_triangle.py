#!/usr/bin/python3
"""abokhadra pascal's algorithm"""


def pascal_triangle(n):
    """a list of lists, each cell in a list
    is the sum of the above 2 cells
    """
    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(2, n + 1):
        a_list = [None] * i
        a_list[0] = 1
        a_list[-1] = 1
        idx = 1
        for j in range(0, len(pascal[-1])):
            if j == len(pascal[-1]) - 1:
                break
            a_list[idx] = pascal[-1][j] + pascal[-1][j + 1]
            idx += 1
        pascal.append(list(a_list))
    return pascal
