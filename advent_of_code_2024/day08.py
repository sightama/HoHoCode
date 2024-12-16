from copy import deepcopy
from collections import deque, defaultdict
from typing import List
from itertools import product, combinations

DAY = 8

# NOTE: I HATE THIS PROBLEM. DAY 8 PART2 I COPPED OUT. NOT SURE WHAT WRONG WITH MY SOLUTION WILL TALK MARK LATER :)

class AdventCode:
    visited = {}
    antennas = set()

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

    def part2(self, inn: str):
        matrix = self.build_matrix(inn)
        antinodes = 0
        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] != '.':
                    letter = matrix[y][x]
                    if letter in self.visited:
                        new_antinode_count, visited = self.explore_two(matrix, x, y, letter, set())
                        self.visited[letter] = self.visited[letter] | visited
                    else:
                        new_antinode_count, visited = self.explore_two(matrix, x, y, letter, set())
                        self.visited[letter] = visited
                    antinodes += new_antinode_count
        final_out = set()
        for x in self.visited.values():
            final_out = final_out | x
        return len(final_out)

    def explore_two(self, matrix: List[List], x, y, node, visited: set):
        total = 0
        # find all other pos with same char
        for new_y in range(len(matrix)):
            for new_x in range(len(matrix[0])):
                if (x != new_x and new_y != y) and node == matrix[new_y][new_x] and (new_x, new_y) not in visited:
                    # keep iterating til out of bound for each
                    dx, dy = new_x - x, new_y - y
                    anti_x, anti_y = dx + new_x, dy + new_y
                    while True:
                        if not (anti_y < 0 or anti_x < 0 or anti_y >= len(matrix) or anti_x >= len(matrix[0])):  # and (anti_x, anti_y) not in visited:
                            visited.add((anti_x, anti_y))
                            if (x, y) not in visited:  # if we got here means we found antinode, let's add original antenna as an antinode then...
                                visited.add((x, y))
                            total += 1
                        else:
                            break
                        anti_x, anti_y = dx + anti_x, anti_y + dy
                    dx, dy = dx * -1, dy * -1
                    anti_x, anti_y = dx + x, dy + y
                    while True:
                        if not (anti_y < 0 or anti_x < 0 or anti_y >= len(matrix) or anti_x >= len(matrix[0])):  # and (anti_x, anti_y) not in visited:
                            visited.add((anti_x, anti_y))
                            if (new_x, new_y) not in visited:  # if we got here means we found antinode, let's add original antenna as an antinode then...
                                visited.add((x, y))
                            total += 1
                        else:
                            break
                        anti_x, anti_y = dx + anti_x, anti_y + dy

        return total, visited

    def part2_tryagain_connor_help(self, inn):
        total_antinodes = set()
        antennas = defaultdict(list)
        for y, row in enumerate(open("./advent_of_code_2024/inputs/day8.txt").read().splitlines()):
            # for y, row in enumerate(test_input.splitlines()):
            max_y = y
            for x, c in enumerate(row):
                max_x = x
                if c != ".":
                    antennas[c].append((x, y))

        for antenna in antennas.values():
            for a, b in combinations(antenna, 2):
                # Calculate the distance between the two antennas
                wavelength = a[0] - b[0], a[1] - b[1]

                # Calculate antinodes for a
                antinode = a[0] - wavelength[0], a[1] - wavelength[1]
                while 0 <= antinode[0] <= max_x and 0 <= antinode[1] <= max_y:
                    total_antinodes.add(antinode)
                    antinode = antinode[0] - wavelength[0], antinode[1] - wavelength[1]

                # Calculate antinodes for b
                antinode = b[0] + wavelength[0], b[1] + wavelength[1]
                while 0 <= antinode[0] <= max_x and 0 <= antinode[1] <= max_y:
                    total_antinodes.add(antinode)
                    antinode = antinode[0] + wavelength[0], antinode[1] + wavelength[1]

        print(len(total_antinodes))
