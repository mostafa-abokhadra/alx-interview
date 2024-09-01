#!/usr/bin/python3
"""
N queens
"""
import sys


def valid(curr, row, col):
    """
    Functions that checks if we can
    place a queen on a certein square
    """
    for r, c in curr:
        if r == row or c == col or abs(r - row) == abs(c - col):
            return False
    return True


def nqueens(n, row=0, curr=None):
    """
    Recursive solution for the N-queens problem
    """
    if curr is None:
        curr = []

    # Base case: All queens are placed
    if row == n:
        print(curr)
        return

    for col in range(n):
        if valid(curr, row, col):
            curr.append([row, col])  # Place the queen
            nqueens(n, row + 1, curr)  # Recur to place the next queen
            curr.pop()  # Backtrack: remove the queen and try the next column


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens(n)
