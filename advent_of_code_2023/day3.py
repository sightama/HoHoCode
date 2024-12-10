from collections import deque
from copy import deepcopy
import string

class AdventCode:
    visited = set()

    def is_symbol(self, char):
        return char in (set(string.punctuation) - {'.'})

    def string_to_2d_map(self, input_string, width):
        # Calculate the number of rows
        input_string = input_string.replace('\n', '')
        height = len(input_string) // width
        # Create a 2D map
        two_d_map = [list(input_string[i * width:(i + 1) * width]) for i in range(height)]
        return two_d_map

    def part1(self, inn: str):  # Took about 1 hr and 4 min
        parts = []
        inn = inn.strip()
        lines = inn.split('\n')
        width = len(lines[0])
        d_map = self.string_to_2d_map(inn, width)
        for line in d_map:
            print(line)
        part_number = None
        for x in range(len(d_map)):
            for y in range(len(d_map[0])):
                if (x, y) not in self.visited:
                    if 0 <= x < len(d_map) and 0 <= y < len(d_map[0]) and d_map[x][y].isdigit():
                        part_number = self.explore(d_map, x, y)
                if part_number:
                    parts.append(part_number)
                    part_number = None

        return sum(parts)

    def explore(self, d_map, x, y):
        self.visited = set()
        number = ''
        valid = False
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            val = d_map[x][y]
            if val.isdigit():
                number += val
            else:
                break
            # up
            if 0 <= x - 1 < len(d_map) and (x-1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y]):
                    valid = True
            # down
            if 0 <= x + 1 < len(d_map) and (x+1, y) not in self.visited:
                if self.is_symbol(d_map[x+1][y]):
                    valid = True
            # left
            if 0 <= y - 1 < len(d_map[0]) and (x, y-1) not in self.visited:
                if self.is_symbol(d_map[x][y-1]):
                    valid = True
            # right
            if 0 <= y + 1 < len(d_map[0]) and (x, y+1) not in self.visited:
                if self.is_symbol(d_map[x][y+1]):
                    valid = True
                queue.append((x, y + 1))

            # DIAGONALS
            # upleft
            if 0 <= x - 1 < len(d_map) and 0 <= y - 1 < len(d_map[0]) and (x-1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y-1]):
                    valid = True
            # upright
            if 0 <= x - 1 < len(d_map) and 0 <= y + 1 < len(d_map[0]) and (x+1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y+1]):
                    valid = True
            # downleft
            if 0 <= y - 1 < len(d_map[0]) and 0 <= x + 1 < len(d_map) and (x, y-1) not in self.visited:
                if self.is_symbol(d_map[x+1][y-1]):
                    valid = True
            # downright
            if 0 <= y + 1 < len(d_map[0]) and 0 <= x + 1 < len(d_map) and (x, y+1) not in self.visited:
                if self.is_symbol(d_map[x+1][y+1]):
                    valid = True

            self.visited.add((x, y))

        if valid:
            return int(number)
        return False


    def part2(self, inn: str):  # Took about 1 hr and 4 min
        parts = []
        inn = inn.strip()
        lines = inn.split('\n')
        width = len(lines[0])
        d_map = self.string_to_2d_map(inn, width)
        for line in d_map:
            print(line)
        part_number = None
        for x in range(len(d_map)):
            for y in range(len(d_map[0])):
                if (x, y) not in self.visited:
                    if 0 <= x < len(d_map) and 0 <= y < len(d_map[0]) and d_map[x][y].isdigit():
                        part_number = self.explore2(d_map, x, y)
                if part_number:
                    parts.append(part_number)
                    part_number = None
        result = []
        visited = set()
        for part in parts:
            test = deque(deepcopy(parts))
            if part in visited:
                continue
            current_val = part[0]
            pos = part[1]
            found = False
            while not found and test:
                a_val, pos2 = test.popleft()
                if a_val == current_val and pos == pos2:
                    continue
                if a_val != current_val and pos == pos2:
                    visited.add((current_val, pos))
                    visited.add((a_val, pos2))
                    result.append(current_val * a_val)
                    found = True
                # else:
                #     test.append((a_val, pos2))

        return sum(result)

    def explore2(self, d_map, x, y):
        self.visited = set()
        number = ''
        valid = False
        symbolq = deque()
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            val = d_map[x][y]
            if val.isdigit():
                number += val
            else:
                break
            # up
            if 0 <= x - 1 < len(d_map) and (x-1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y]):
                    valid = True
                    symbolq.append((x-1, y))
            # down
            if 0 <= x + 1 < len(d_map) and (x+1, y) not in self.visited:
                if self.is_symbol(d_map[x+1][y]):
                    valid = True
                    symbolq.append((x+1, y))

            # left
            if 0 <= y - 1 < len(d_map[0]) and (x, y-1) not in self.visited:
                if self.is_symbol(d_map[x][y-1]):
                    valid = True
                    symbolq.append((x, y-1))

            # right
            if 0 <= y + 1 < len(d_map[0]) and (x, y+1) not in self.visited:
                if self.is_symbol(d_map[x][y+1]):
                    valid = True
                    symbolq.append((x, y+1))
                queue.append((x, y + 1))

            # DIAGONALS
            # upleft
            if 0 <= x - 1 < len(d_map) and 0 <= y - 1 < len(d_map[0]) and (x-1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y-1]):
                    valid = True
                    symbolq.append((x-1, y-1))

            # upright
            if 0 <= x - 1 < len(d_map) and 0 <= y + 1 < len(d_map[0]) and (x+1, y) not in self.visited:
                if self.is_symbol(d_map[x-1][y+1]):
                    valid = True
                    symbolq.append((x-1, y+1))

            # downleft
            if 0 <= y - 1 < len(d_map[0]) and 0 <= x + 1 < len(d_map) and (x, y-1) not in self.visited:
                if self.is_symbol(d_map[x+1][y-1]):
                    valid = True
                    symbolq.append((x+1, y-1))

            # downright
            if 0 <= y + 1 < len(d_map[0]) and 0 <= x + 1 < len(d_map) and (x, y+1) not in self.visited:
                if self.is_symbol(d_map[x+1][y+1]):
                    valid = True
                    symbolq.append((x+1, y+1))

            self.visited.add((x, y))

        if valid:
            # if len(symbolq) > 1:
            #     print('YOU FAILEED THERES MORE THENE ONE SYMBOL TO A GIVEN NUMBER!')
            x, y = symbolq.popleft()
            if d_map[x][y] == '*':
                return int(number), (x, y)
            else:
                return False
        return False
