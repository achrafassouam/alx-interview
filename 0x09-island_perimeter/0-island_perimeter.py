#!/usr/bin/python3
"""
define the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    return the perimeter
    """
    perimiter = 0
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:

                perimiter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimiter -= 1

                if r < rows - 1 and grid[r+1][c] == 1:
                    perimiter -= 1

                if c > 0 and grid[r][c-1] == 1:
                    perimiter -= 1

                if c < cols and grid[r][c+1] == 1:
                    perimiter -= 1

    return perimiter
