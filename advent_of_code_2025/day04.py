from collections import deque, Counter
from copy import deepcopy

DAY = 4


class AdventCode:

    # (16 min)
    @staticmethod
    def part1(inn: str):
        result = 0
        # bfs - shortest path only looking at adj points, need to be <4 rolls (@) not including the @ we are at.
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # all 8 adjencts
        # make sure to check within bounds on all points
        grid = inn.strip().split('\n')
        grid = [list(x) for x in grid]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '@':
                    rolls = 0
                    for dx, dy in delta:
                        if not (0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid)): # bounding
                            continue
                        if grid[dy+y][dx+x] == '@':
                            rolls += 1
                    if rolls < 4:
                        result += 1
        return result

    # 6 minutes
    @staticmethod
    def part2(inn: str):
        result = 0
        delta = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]  # all 8 adjencts
        grid = [list(x) for x in inn.strip().split('\n')]
        can_get_rolls = {(0, 0)}  # just to get into loop...
        while can_get_rolls:
            can_get_rolls = set()
            for y in range(len(grid)):
                for x in range(len(grid[0])):
                    if grid[y][x] == '@':
                        rolls = 0
                        for dx, dy in delta:
                            if not (0 <= x+dx < len(grid[0]) and 0 <= y+dy < len(grid)): # bounding
                                continue
                            if grid[dy+y][dx+x] == '@':
                                rolls += 1
                        if rolls < 4:
                            result += 1
                            can_get_rolls.add((x, y))
            # mark points
            for mark_x, mark_y in can_get_rolls:
                grid[mark_y][mark_x] = '.'
        return result
