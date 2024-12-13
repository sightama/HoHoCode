from copy import deepcopy
from collections import deque, defaultdict
from typing import List
from itertools import product

DAY = 8


class AdventCode:
    visited = {}

    def build_matrix(self, inn: str):
        matrix = inn.split('\n')
        matrix = [list(x) for x in matrix]
        return matrix

    def part1(self, inn: str):
        matrix = self.build_matrix(inn)
        antinodes = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] != '.':
                    letter = matrix[y][x]
                    if letter in self.visited:
                        new_antinode_count, visited = self.explore(matrix, x, y, letter, self.visited[letter])
                        self.visited[letter] = self.visited[letter] | visited
                    else:
                        new_antinode_count, visited = self.explore(matrix, x, y, letter, set())
                        self.visited[letter] = visited
                    antinodes += new_antinode_count
        final_out = set()
        for x in self.visited.values():
            final_out = final_out | x


        return len(final_out)

    def explore(self, matrix: List[List], x, y, node, visited: set):
        total = 0
        # find all other pos with same char
        for new_y in range(len(matrix)):
            for new_x in range(len(matrix[0])):
                if (x != new_x and new_y != y) and node == matrix[new_y][new_x] and (new_x, new_y) not in visited:
                    # calculate distance delta
                    # visited.add((new_x, new_y))
                    dx, dy = new_x - x, new_y - y
                    anti_x, anti_y = dx + new_x, dy + new_y
                    if not (anti_y < 0 or anti_x < 0 or anti_y >= len(matrix) or anti_x >= len(matrix[0])) and (
                            anti_x, anti_y) not in visited:
                        visited.add((anti_x, anti_y))
                        total += 1
                    dx, dy = dx * -1, dy * -1
                    anti_x, anti_y = dx + x, dy + y
                    if not (anti_y < 0 or anti_x < 0 or anti_y >= len(matrix) or anti_x >= len(matrix[0])) and (
                            anti_x, anti_y) not in visited:
                        visited.add((anti_x, anti_y))
                        total += 1
        return total, visited
