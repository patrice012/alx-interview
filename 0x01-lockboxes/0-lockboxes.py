#!/usr/bin/python3
"""
0x01. Lockboxes -- solution
"""


def canUnlockAll(boxes: list[list]) -> bool:
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

    set_of_keys = set()
    set_of_keys.add(0)
    queue = [0]

    for key in queue:
        for new_key in boxes[key]:
            if new_key not in set_of_keys:
                set_of_keys.add(new_key)
                queue.append(new_key)
    return len(set_of_keys) == len(boxes)
