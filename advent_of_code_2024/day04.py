from collections import deque
from typing import List
from copy import copy, deepcopy

def read_file_to_string(file_path):
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
        return file_contents
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except IOError as e:
        print(f"Error reading the file: {e}")

def build_matrix(inn: str):
    rows = inn.split('\n')
    matrix = []
    for row in rows:
        chars = list(row)
        matrix.append(chars)
    return matrix


def explore_bfs(matrix: List, pos: tuple, letters: deque, direction = None):
    total = 0
    if not letters:
        return 0
    next_letter = letters.popleft()
    delta = {'r': (1, 0), 'l': (-1, 0), 'u': (0, 1), 'd': (0, -1), 'br': (1, 1), 'bl': (-1, 1), 'tl': (-1, -1), 'tr': (1, -1)}
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_input = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""
    test_input = read_file_to_string(f"./input.txt")
    total = part1(test_input)
    print(f"Result = {total}")