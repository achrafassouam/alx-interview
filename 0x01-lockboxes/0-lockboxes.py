#!/usr/bin/python3
"""
A function that determines if all the boxes can be opened given a list of keys

The function returns `True` if all boxes can be opened, and `False` otherwise
"""


def canUnlockAll(boxes):
    """Determines if all the boxes can be opened given a list of keys."""

    n = len(boxes)
    opened = [False] * n
    opened[0] = True

    keys = set(boxes[0])

    while True:
        new_keys = False
        for key in list(keys):
            if key < n and not opened[key]:
                opened[key] = True
                keys.update(boxes[key])
                new_keys = True
        if not new_keys:
            break

    return all(opened)
