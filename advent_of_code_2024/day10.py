from collections import deque, defaultdict
from typing import List
from copy import deepcopy

DAY = 10

""" 
GENERAL NOTES:
pt1 bug:
FOUND IT. CODE MADE IN 1 HOUR, 40 MINUTES TO DEBUG I HAD RETURN IN RECURSE_DFS -> IF NEXTSTEP==0 RETURN. 
nope we want to check all u|d|l|r for all 0s surrounding a 1, not just the first. so removeed return g2g
"""


class AdventCode:
    # this will be tuple as key (pos of 0 spot), trailhead count as value (only 0 values should be logged here.
    hiking_trails = defaultdict(int)
    matrix: List
    deltas = {'d': (0, 1), 'u': (0, -1), 'l': (-1, 0), 'r': (1, 0)}  # constraints: up, down, left, right

    def make_num_matrix(self, inn: str):
        rows = inn.strip().split('\n')
        self.matrix = [list(x) for x in rows]
        self.matrix = [[int(char) for char in row] for row in self.matrix]

    def part1(self, inn: str):
        self.make_num_matrix(inn)
        for y in range(len(self.matrix)):  # iterate through all rows finding a 9.
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x] == 9:
                    self.recurse_dfs(x, y, deepcopy(deque([8, 7, 6, 5, 4, 3, 2, 1, 0])), deepcopy(set()))

        # self.order_dict()
        return sum(self.hiking_trails.values())

    def recurse_dfs(self, x: int, y: int, height: deque, visited: set):
        if not height:
            return

        neighbors = list()
        for dx, dy in self.deltas.values():  # track pos, number on, and all deltas
            next_x = dx + x
            next_y = dy + y
            if next_y < 0 or next_x < 0 or next_y >= len(self.matrix) or next_x >= len(self.matrix[0]):
                # constraint: not out of bound
                continue  # this is boundary check. If fails don't even add to queue
            neighbors.append((next_x, next_y))

        queue = deque(neighbors)
        next_step = height.popleft()
        while queue:  # constraint: next number must decrement until 0. if 0 hit, add to dict above, otherwise new entry
            cur_x, cur_y = queue.popleft()

            if next_step == 0 and self.matrix[cur_y][cur_x] == next_step and (cur_x, cur_y) not in visited:
                self.hiking_trails[(cur_x, cur_y)] += 1  # this is beginning/trailhead
                visited.add((cur_x, cur_y))

            if next_step == self.matrix[cur_y][cur_x]:  # found next decrement go downhill
                self.recurse_dfs(cur_x, cur_y, deepcopy(height), visited)

    def order_dict(self):
        """ chatgpt made this for me to debug easier. absolutely not needed """
        # Sort the defaultdict by its keys (x, y) in ascending order
        sorted_data = dict(sorted(self.hiking_trails.items(), key=lambda item: (item[0][1], item[0][0])))
        for key, value in sorted_data.items():
            print(f"Position {key}: Value {value}")

    def part2(self, inn: str):
        self.make_num_matrix(inn)
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                if self.matrix[y][x] == 9:
                    self.recurse_dfs_2(x, y, deepcopy(deque([8, 7, 6, 5, 4, 3, 2, 1, 0])), deepcopy(set()))

        self.order_dict()
        return sum(self.hiking_trails.values())

    def recurse_dfs_2(self, x: int, y: int, height: deque, visited: set):
        if not height:
            return
        neighbors = list()
        for dx, dy in self.deltas.values():
            next_x = dx + x
            next_y = dy + y
            if next_y < 0 or next_x < 0 or next_y >= len(self.matrix) or next_x >= len(self.matrix[0]):
                continue
            neighbors.append((next_x, next_y))
        queue = deque(neighbors)
        next_step = height.popleft()
        while queue:
            cur_x, cur_y = queue.popleft()
            if next_step == 0 and self.matrix[cur_y][cur_x] == next_step:  # and (cur_x, cur_y) not in visited:
                self.hiking_trails[(cur_x, cur_y)] += 1
                visited.add((cur_x, cur_y))
            if next_step == self.matrix[cur_y][cur_x]:
                self.recurse_dfs_2(cur_x, cur_y, deepcopy(height), visited)
