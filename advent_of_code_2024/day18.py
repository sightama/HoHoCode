from copy import deepcopy
from collections import deque

DAY = 18

MAX_X = 0
MAX_Y = 0


class AdventCode:
    smallest_answer_so_far = 1e99

    def part1(self, inn: str):
        # pts = {}
        Y = 71  #
        X = 71  #
        matrix = [['.' for _ in range(X)] for _ in range(Y)]
        # parse input
        rows = inn.split('\n')
        for i, row in enumerate(rows):
            if i == 1024:
                break  # first 1024 "bytes" in the large list of "bytes" for input.
            test = row.split(',')
            x, y = int(test[0]), int(test[1])
            # pts[i] = (x, y)
            matrix[y][x] = '#'

        # recursive dfs to find paths
        # smallest_steps = self.explore_dfs(matrix, 0, 0, 1, 1e99, set())  # x, y, steps, direction
        shorest_path = self.bfs(matrix, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)
        return shorest_path

    # NOTE: too expensive, works for sample 12 bytes but NOT for larger set. seems to get stuck.
    # def explore_dfs(self, matrix, x, y, steps, smallest_steps, visited):
    #     print(F"CURRENT (X,Y) = ({x}, {y}) \t with STEPS = {steps}")
    #     delta = {'r': (1, 0), 'u': (0, -1), 'd': (0, 1), 'l': (-1, 0)}
    #     visited.add((x, y))
    #     MAX_Y = len(matrix)
    #     MAX_X = len(matrix[0])
    #     for direction, (dx, dy) in delta.items():
    #         new_x, new_y = dx + x, dy + y
    #         if new_x < 0 or new_y < 0 or new_x >= MAX_X or new_y >= MAX_Y:
    #             continue  # outofbounds
    #         if new_x == MAX_X - 1 and new_y == MAX_Y - 1:
    #             if steps < self.smallest_answer_so_far:
    #                 self.smallest_answer_so_far = steps
    #             return steps
    #
    #         if matrix[new_y][new_x] == '#':
    #             continue  # deadeendgetfucked
    #         if matrix[new_y][new_x] == '.' and (new_x, new_y) not in visited:
    #             # valid spot recurse
    #             if steps + 1 >= self.smallest_answer_so_far:
    #                 continue
    #             new_steps = self.explore_dfs(matrix, new_x, new_y, steps + 1, smallest_steps, deepcopy(visited))
    #             if new_steps and new_steps < smallest_steps:
    #                 smallest_steps = new_steps
    #     return smallest_steps  # Got here means deadend

    def bfs(self, grid, start_x, start_y, gx, gy):
        queue = deque([(start_x, start_y, 0)])
        seen = {(start_x, start_y)}
        while queue:
            x, y, steps = queue.popleft()
            if y == gy and x == gx:
                return steps
            for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
                if 0 <= x2 < len(grid[0]) and 0 <= y2 < len(grid) and grid[y2][x2] != '#' and (x2, y2) not in seen:
                    queue.append((x2, y2, steps + 1))
                    seen.add((x2, y2))
        return None  # not possible


    def part2(self, inn: str):
        # pts = {}
        Y = 71  #
        X = 71  #
        matrix = [['.' for _ in range(X)] for _ in range(Y)]
        # parse input
        rows = inn.split('\n')
        for i, row in enumerate(rows):
            # if i == 1024:
            #     break  # first 1024 "bytes" in the large list of "bytes" for input.
            test = row.split(',')
            x, y = int(test[0]), int(test[1])
            # pts[i] = (x, y)
            matrix[y][x] = '#'
            shortest_path = self.bfs(matrix, 0, 0, len(matrix[0]) - 1, len(matrix) - 1)
            if shortest_path is None:
                return (x, y)  # answer

        # recursive dfs to find paths
        # smallest_steps = self.explore_dfs(matrix, 0, 0, 1, 1e99, set())  # x, y, steps, direction

        return shortest_path