from collections import deque, Counter
from copy import deepcopy

DAY = 1


class AdventCode:
    # took about 30 minutes.
    @staticmethod
    def part1(inn: str):
        num_of_zeroes = 0
        pos = 50
        new_pos = 0  # just to get rid of reference before assign msg.
        moves = inn.split('\n')
        queue = deque(moves)
        while queue:
            cur = queue.popleft()
            direction, steps = cur[0], cur[1:]
            # we just need the last two of the numbers. ie 524 -> 24, 148 -> 48.
            if len(steps) > 2:
                steps = steps[-2:]
            steps = int(steps)

            if direction == 'R':
                new_pos = steps + pos
                if new_pos > 99:
                    new_pos = new_pos - 100
            elif direction == 'L':
                new_pos = pos - steps
                if new_pos < 0:
                    new_pos = new_pos + 100

            if new_pos == 0:
                num_of_zeroes += 1
            pos = new_pos
        return num_of_zeroes

    # took an hour, started using part1 solution to realize better solution was brute force.
    @staticmethod
    def part2(inn: str):
        num_of_zeroes = 0
        pos = 50
        moves = inn.split('\n')
        queue = deque(moves)
        while queue:
            cur = queue.popleft()
            direction, steps = cur[0], int(cur[1:])
            while steps:
                # 1. make step
                if direction == 'L':
                    steps -= 1
                    pos -= 1
                elif direction == 'R':
                    steps -= 1
                    pos += 1
                # 2. stay within bounds of safe lock (0-99)
                if pos == -1:
                    pos = 99
                elif pos == 100:
                    pos = 0
                # 3. did we hit a zero? no? keep going.
                if pos == 0:
                    num_of_zeroes += 1
        return num_of_zeroes
