#!/usr/bin/python3


def recursive_land(grid, i, j, total):
    """
        recursive function to check the total of params
        Args:
            i: row
            j: column
            total: total of params
        Return - total of params
    """
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
        return total

    if grid[i][j] == 2 or grid[i][j] == 0:
        return total

    if i - 1 == -1:
        total += 1
    else:
        up = grid[i - 1][j]
        if up == 0:
            total += 1

    if j - 1 == -1:
        total += 1
    else:
        left = grid[i][j - 1]
        if left == 0:
            total += 1

    if j + 1 == len(grid[0]):
        total += 1
    else:
        right = grid[i][j + 1]
        if right == 0:
            total += 1

    if i + 1 == len(grid):
        total += 1
    else:
        bottom = grid[i + 1][j]
        if bottom == 0:
            total += 1

    grid[i][j] = 2

    total = recursive_land(grid, i - 1, j, total)
    total = recursive_land(grid, i + 1, j, total)
    total = recursive_land(grid, i, j - 1, total)
    total = recursive_land(grid, i, j + 1, total)
    return total


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    for i in range(len(grid)):
        for y in range(len(grid[i])):
            if grid[i][y] == 1:
                break
        if grid[i][y]:
            break
    total = recursive_land(grid, i, y, 0)
    return total
