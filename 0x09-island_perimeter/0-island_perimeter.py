#!/usr/bin/python3
"""
define the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    return the perimeter
    """
    cols = len(grid[0])
    rows = len(grid)
    size = 0
    edge = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                size += 1
                if (c > 0 and grid[r][c - 1] == 1):
                    edge += 1
                if (r > 0 and grid[r - 1][c] == 1):
                    edge += 1
    return size * 4 - edge * 2
