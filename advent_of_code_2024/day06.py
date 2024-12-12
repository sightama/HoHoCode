from copy import deepcopy
from collections import deque, defaultdict
from typing import List

DAY = 6


class AdventCode:
    direction = {'^': 'u', 'v': 'd', '<': 'l', '>': 'r'}
    delta = {'u': (0, -1), 'd': (0, 1), 'l': (-1, 0), 'r': (1, 0)}
    switch = {'r': 'd', 'd': 'l', 'l': 'u', 'u': 'r'}

    def part1(self, inn: str):  # 25m
        total_steps = None
        matrix = self.build_matrix(inn)
        # find guard
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] in self.direction:
                    total_steps = self.explore(matrix, x, y, self.direction[matrix[y][x]])
        return total_steps

    def build_matrix(self, inn: str):
        matrix = inn.split('\n')
        matrix = [list(x) for x in matrix]
        return matrix

    def explore(self, matrix: List[List], x, y, direction):
        # explore until the end
        distinct_pos = {(x, y)}
        while True:  # kek - guaranteed to leave the map area
            dx, dy = self.delta[direction]
            if dx + x < 0 or dy + y < 0 or dy + y >= len(matrix) or dx + x >= len(matrix[0]):
                return len(distinct_pos)  # stop early we got out.
            next_spot = matrix[dy + y][dx + x]
            if next_spot in ['.', '^']:  # ignore original symbol
                x, y = dx + x, dy + y
                distinct_pos.add((x, y))
            if next_spot == '#':
                direction = self.switch[direction]
