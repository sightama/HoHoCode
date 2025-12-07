from collections import deque, Counter
from copy import deepcopy

DAY = 6


class AdventCode:

    @staticmethod  # took 15 min
    def part1(inn: str):
        result = 0
        grid = inn.strip().split('\n')
        operations = grid[-1]
        grid.remove(operations)
        operations = [x for x in operations if not x.isspace()]
        new_grid = []
        for nums in grid:
            row = nums.split(' ')
            row = [int(x) for x in row if x.isdigit()]
            new_grid.append(row)
        for x in range(len(new_grid[0])):
            nums = []  # start first row x = 0 for all y's
            for y in range(len(new_grid)):
                nums.append(new_grid[y][x])
            if operations[x] == '*':
                final = 1
                for i in nums:
                    final *= i
            if operations[x] == '+':
                final = 0
                for i in nums:
                    final += i
            result += final
        return result

    @staticmethod
    def part2(inn: str):
        pass
