#!/usr/bin/python3
"""
    problem solving - lockedBoxes module
    You have n number of locked boxes in front of you.
    Each box is numbered sequentially from 0 to n - 1.
    each box may contain keys to the other boxes.
    A key with the same number as a box opens that box.
    There can be keys that do not have boxes.
    The first box boxes[0] is unlocked.
    task: determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    
    Args:
        boxes: list of lists

    Returns:
        true if all boxes can be opened
        else return False
    """
    [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]