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

    def part2(self, inn: str):
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

        r, rr = len(full) - 1, len(full) - 1
        l, ll = 0, 0
        visited = set()
        while l+1 != r:
            l, ll = 0, 0
            if r <= 0:
                break  # idk why while loop not do what want, but this should work.
            # get right side file size
            while full[r] == '.':
                print(r)
                r -= 1
            rr = r
            val = full[r]
            if val in visited:
                r -=1  # iterate once to get to next node left; we've already seen thise node
                continue
            visited.add(val)
            while full[rr] == val:
                rr -= 1
            # rr r is range of file above.
            filesize = r - rr


            # THEN find a salot from left ro right that fits it (before file itself). if nothing SKIP IT.
            while l <= rr:
                if full[l] != '.':
                    l += 1
                    continue
                else:
                    ll = l
                    while full[ll] == '.':
                        ll += 1
                        continue
                    window_size = ll - l
                    if window_size >= filesize:
                        diff = window_size - filesize
                        for i in range(l, ll-diff):
                            full[i] = val
                        for i in range(rr+1, r+1):
                            full[i] = '.'
                        break
                    else:
                        l = ll
                        continue
            r = rr  # set to look at next file and its filesize

        # FULL is the fully organized fule-compacting processe.
        # Calculate the filesystem checksum
        total = 0
        for i, x in enumerate(full):
            if x != '.':
                total += int(x) * i

        return total
