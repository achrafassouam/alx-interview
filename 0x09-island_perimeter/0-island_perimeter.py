#!/usr/bin/python3
"""
define the perimeter of the island described in grid
"""

def island_perimeter(grid):
	perimiter = 0
	rows = len(grid)
	cols = len(grid[0])

	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == 1:
				# full perimeter of 4 for a land cell
				perimiter += 4

				#Check for neighboring land cells
				#up
				if r > 0 and grid[r-1][c] == 1:
					perimiter -= 1
				#down
				if r < rows - 1 and grid[r+1][c] == 1:
					perimiter -= 1
				#left
				if c > 0 and grid[r][c-1] == 1:
					perimiter -= 1
				#Right
				if c < 0 and grid[r][c+1] == 1:
					perimiter -= 1
	
	return perimiter
