from collections import deque
from typing import List
from copy import copy, deepcopy

DAY = 4


class AdventCode:
    matrix: List

    @staticmethod
    def part1(inn: str):
        total = 0
        # build a matrix in list
        matrix = build_matrix(inn)
        for y, row in enumerate(matrix):
            queue = deque(row)
            x = 0
            while queue:
                current = queue.popleft()
                if current == 'X':
                    # check for all cases to find M
                    pos = (x, y)
                    test = copy(deque(['M', 'A', 'S']))
                    how_many_row = explore_bfs(matrix, pos, test)
                    total += how_many_row
                x += 1
        return total

    def part2(self, inn: str):
        total = 0
        self.matrix = build_matrix(inn)
        for y, row in enumerate(self.matrix):
            queue = deque(row)
            x = 0
            while queue:
                current = queue.popleft()
                if current == 'A':
                    pos = (x, y)
                    valid = self.is_valid_cross_mas(pos)
                    if valid:
                        total += 1

                x += 1
        return total

    def is_valid_cross_mas(self, a_pos: tuple):
        flip = {'br': 'tl', 'tl': 'br', 'tr': 'bl', 'bl': 'tr'}
        letter_map = {'M': 'S', 'S': 'M'}
        delta = {'br': (1, 1), 'bl': (-1, 1), 'tl': (-1, -1), 'tr': (1, -1)}
        options = {}
        for k, v in delta.items():
            an_option = tuple(x + y for x, y in zip(a_pos, v))
            options[k] = an_option
        for direction, pos in options.items():
            x, y = pos
            if x >= len(self.matrix[0]) or y >= len(self.matrix) or x < 0 or y < 0:
                return False  # If its the case that one of the diagonals next to A is out of bounds, false.

            letter = self.matrix[y][x]
            if letter not in {'M', 'S'}:
                return False

            diagonal_letter = letter_map[letter]
            diagonal_x, diagonal_y = options[flip[direction]]
            if self.matrix[diagonal_y][diagonal_x] == diagonal_letter:
                continue
            else:
                return False  # just get out. not a valid configuration. LEAVE EARLY

        return True


def build_matrix(inn: str):
    rows = inn.split('\n')
    matrix = []
    for row in rows:
        chars = list(row)
        matrix.append(chars)
    return matrix


def explore_bfs(matrix: List, pos: tuple, letters: deque, direction=None):
    total = 0
    if not letters:
        return 0
    next_letter = letters.popleft()
    delta = {'r': (1, 0), 'l': (-1, 0), 'u': (0, 1), 'd': (0, -1), 'br': (1, 1), 'bl': (-1, 1), 'tl': (-1, -1),
             'tr': (1, -1)}
    options = []
    if direction:
        options.append((direction, tuple(x + y for x, y in zip(pos, delta[direction]))))
    else:  # Check all direction for 'X'
        for k, v in delta.items():
            an_option = tuple(x + y for x, y in zip(pos, v))
            options.append((k, an_option))
    queue = deque(options)
    while queue:
        direction, pos = queue.popleft()
        x, y = pos
        if x >= len(matrix[0]) or y >= len(matrix) or x < 0 or y < 0:
            continue
        letter = matrix[y][x]
        if letter == next_letter:
            if letter == 'S':
                return 1
            else:
                total += explore_bfs(matrix, (x, y), deepcopy(letters), direction)
    # look for x in BFS
    # create a directional delta that goes diagonally, left right up down for M -> A -> S
    return total
