#!/usr/bin/python3
def pascal_triangle(n):
    if n <= 0:
        return []
    a_list = []
    pascal = [[1], [1, 1]]
    idx = 0
    for i in range(3, n + 1):
        a_list = [None] * i
        a_list[0] = 1
        a_list[-1] = 1
        idx = 1
        for j in range(0, len(pascal[-1])):
            if j == len(pascal[-1]) - 1:
                break;
            a_list[idx] = pascal[-1][j] + pascal[-1][j + 1]
            idx += 1
        pascal.append(list(a_list))
    return pascal