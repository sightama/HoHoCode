from copy import deepcopy
from collections import deque, defaultdict
from typing import List
from tqdm import tqdm

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
                    total_steps, distinct_pos, boxes = self.explore(matrix, x, y, self.direction[matrix[y][x]])
        return total_steps

    def build_matrix(self, inn: str):
        matrix = inn.split('\n')
        matrix = [list(x) for x in matrix]
        return matrix

    def explore(self, matrix: List[List], x, y, direction):
        # explore until the end
        distinct_pos = {(x, y)}
        distinct_boxes = set()
        while True:  # kek - guaranteed to leave the map area
            dx, dy = self.delta[direction]
            if dx + x < 0 or dy + y < 0 or dy + y >= len(matrix) or dx + x >= len(matrix[0]):
                return len(distinct_pos), distinct_pos, distinct_boxes  # stop early we got out.
            next_spot = matrix[dy + y][dx + x]
            if next_spot in ['.', '^']:  # ignore original symbol
                x, y = dx + x, dy + y
                distinct_pos.add((x, y))
            if next_spot == '#':
                distinct_boxes.add((dx + x, dy + y))
                direction = self.switch[direction]

    def part2(self, inn: str):
        # we know there are 4515 distinct steps that are walker hits
        # everytime we visit a box and turn, record it as visited including placed one. if we hit at least 1 full rotation  and the same placed object after
        total_steps = None
        matrix = self.build_matrix(inn)
        # find guard
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] in self.direction:
                    total_steps, distinct_pos, boxes = self.explore(matrix, x, y, self.direction[matrix[y][x]])
                    how_many_obstructions = self.explore_and_find(matrix, x, y, distinct_pos)
        return how_many_obstructions

    def explore_and_find(self, matrix: List[List], x, y, distinct_pos):
        # explore until the end
        loops = set()
        og_x, og_y = x, y
        # distinct_pos = {(3, 6), (6, 7), (7, 7), (1, 8), (3, 8), (7, 9)}

        for box_x, box_y in distinct_pos:
            # reset values below.
            visited = defaultdict(int)  # key pos, value count.
            matrix[box_y][box_x] = '#'
            direction = 'u'
            x, y = og_x, og_y
            iteration = 0
            visited_count = 0

            while True:  # kek - guaranteed to leave the map area
                dx, dy = self.delta[direction]

                if visited_count != len(visited):
                    visited_count = len(visited)
                    iteration = 0
                elif visited_count == len(visited) and iteration == 300:
                    loops.add((box_x, box_y))  # loop - we've had the same number of hit elements for 100x move on.
                    print(f"found loop! Adding box point: {(box_x, box_y)}")
                    break

                if dx + x < 0 or dy + y < 0 or dy + y >= len(matrix) or dx + x >= len(matrix[0]):
                    break  # break early, this is not valid loop.

                next_spot = matrix[dy + y][dx + x]
                if next_spot in ['.', '^']:  # ignore original symbol
                    x, y = dx + x, dy + y
                    visited[(x, y)] += 1
                if next_spot == '#':
                    direction = self.switch[direction]
                iteration += 1

            matrix[box_y][box_x] = '.'

        return len(loops)
