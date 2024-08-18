#!/usr/bin/env python3
from functools import reduce
def add (a, b):
    return a + b

listy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reduce(add, listy))

