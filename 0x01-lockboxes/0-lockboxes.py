#!/usr/bin/python3
"""
0x01. Lockboxes -- solution
"""


def canUnlockAll(boxes):
    """
    Args:
        boxes: list of lists of positive integers
    Returns:
        True if all boxes can be opened, False otherwise
    """

    # Check if boxes is a non-empty list
    if not boxes or not isinstance(boxes, list):
        return False

    # Check if all elements in boxes are lists
    if not all(isinstance(sublist, list) for sublist in boxes):
        return False

    # return true by default if length == 1
    if len(boxes) == 1:
        return True

    keys = [0]
    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < len(boxes):
                keys.append(new_key)
    return len(keys) == len(boxes)
