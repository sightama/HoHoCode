from collections import deque, Counter
from copy import deepcopy

DAY = 7


class AdventCode:
    # create grid, locating starting point. end condition is out-of-bounds or all '^'
    # keep going down til ^, then recurse on new starting point until total splits at end.
    # took 30 min - didnt need a seen set but keklmao overthought it here.
    def part1(self, inn: str):
        start = inn.split('\n')
        grid = []
        for star in start:
            row = []
            for char in star:
                row.append(char)
            grid.append(row)
        start = -1 # find start
        for i, char in enumerate(grid[0]):
            if char == 'S':
                start = i
                break
        seen = set()  # this will hold all split xys.
        splits = self.recurse(start, 1, grid, seen)
        return splits

    def recurse(self, x, y, grid, seen):
        splits = 0  # dfs from point downward until ^ else keep going
        # check edge cases first.
        if (x < 0 or x >= len(grid[0])) or (y < 0 or y >= len(grid)):
            return splits
        
        if grid[y][x] == '.':  # down
            grid[y][x] = '|'
            splits += self.recurse(x, y+1, grid, seen)
        if grid[y][x] == '^':  # right/left
            seen.add((x, y))
            splits += 1
            splits += self.recurse(x+1, y, grid, seen)
            splits += self.recurse(x-1, y, grid, seen)
        return splits

    # took x
    def part2(self, inn: str):
        start = inn.split('\n')
        grid = []
        for star in start:
            row = []
            for char in star:
                row.append(char)
            grid.append(row)
        start = -1 # find start
        for i, char in enumerate(grid[0]):
            if char == 'S':
                start = i
                break
        seen = set()  # this will hold all split xys.
        splits = self.recurseAll(start, 1, grid, seen, '')
        return splits

    def recurseAll(self, x, y, grid, seen, cur_path):
        path = 0  # dfs to the end - this now tracks all times we reach the end
        if cur_path in seen:  # we've hit this path before, skip. optimization.
            return 0 
        if (x < 0 or x >= len(grid[0])) or y >= len(grid):  # check edge cases first.
            seen.add(cur_path)
            return 1 # end of one of our paths
        if grid[y][x] == '.' or grid[y][x] == '|':  # down
            grid[y][x] = '|'
            path += self.recurseAll(x, y+1, grid, seen, cur_path + 'd')
        if grid[y][x] == '^':  # right/left
            path += self.recurseAll(x+1, y, grid, seen, cur_path + 'r')
            path += self.recurseAll(x-1, y, grid, seen, cur_path + 'l')
        return path