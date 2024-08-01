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


def solve(boxes, oneBox, still_locked):
    if len(still_locked) == 0:
        return True
    for key in oneBox:
        if not(key in still_locked):
            continue
        still_locked.remove(key)
        solve(boxes, boxes[key], still_locked)
        if len(still_locked) == 0:
            return True
    return False


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.

    Args:
        boxes: list of lists

    Returns:
        true if all boxes can be opened
        else return False
    """
    all_locked = [i for i in range(1, len(boxes))]
    return solve(boxes, boxes[0], all_locked)
