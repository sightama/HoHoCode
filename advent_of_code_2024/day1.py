from collections import deque, Counter
from typing import List
from copy import copy

DAY = 1


class AdventCode:

    @staticmethod
    def part1(inn: str):
        rows = inn.split('\n')
        left = []
        right = []
        for row in rows:
            rows = row.split('   ')
            left.append(int(rows[0]))
            right.append(int(rows[1]))
        left = sorted(left)
        right = sorted(right)
        left = deque(left)
        right = deque(right)
        sauce = []
        for _ in range(len(left)):
            left_cur = left.popleft()
            right_cur = right.popleft()
            val = abs(left_cur - right_cur)
            sauce.append(val)
        return sum(sauce)

    def part2(self, inn: str):
        rows = inn.split('\n')
        left, right = [], []
        for row in rows:
            rows = row.split('   ')
            left.append(int(rows[0]))
            right.append(int(rows[1]))
        mapp = Counter(right)
        sauce = []
        for x in left:
            if x in mapp:
                sauce.append(x * mapp[x])
        return sum(sauce)
