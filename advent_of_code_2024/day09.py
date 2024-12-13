from copy import deepcopy
from collections import deque, defaultdict
from typing import List
from itertools import product, combinations

DAY = 9


class AdventCode:
    ids = {}  # all dicts are ordered now in my python version; assume ordered.

    def part1(self, inn: str):
        queue = deque(list(inn))
        # first build out ids
        count = 0
        while queue:
            block_size = queue.popleft()
            if queue:
                free_space = queue.popleft()
                free = ['.'] * int(free_space)
            else:  # it can be the case that we don't end on even and instead no free space on last block.
                free = []
            block = [str(count)] * int(block_size)
            block.extend(free)
            self.ids[count] = block
            count += 1

        # transformed = ''.join([x for x in self.ids.values()])
        # use left right pos counter to "trade" spots
        full = []
        for vals in self.ids.values():
            full.extend(vals)
        l = 0
        r = len(full) - 1
        while l != r:
            if full[l] != '.':
                l += 1
                continue

            if full[r] != '.':
                full[l], full[r] = full[r], full[l]
                r -= 1
                l += 1
            else:
                r -= 1
        # FULL is the fully organized fule-compacting processe.
        # Calculate the filesystem checksum
        total = 0
        for i, x in enumerate(full):
            if x != '.':
                total += int(x) * i

        return total
