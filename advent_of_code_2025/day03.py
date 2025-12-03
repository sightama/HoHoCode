from collections import deque, Counter
from copy import deepcopy

DAY = 3


class AdventCode:
    nums = {} # part2
    # (26 min)
    @staticmethod
    def part1(inn: str):
        # steps: 1. find LARGEST number in row NOT INCLUDING THE FINAL NUMBER.
        # step 2: find largest number in row AFTER main largest number and INCLUDING THE FINAL NUMBER.
        # we know: values are only 1-9; final joltage could only be XX, 2 digits. Right digit ALWAYS right of left index.
        # finally sum all max joltages per row to get final answer. (6 min brainstorm)
        #implement: do we need left/right counter? or use one counter and a boolean? either works.
        # time complexity: no worries here I think
        fuck_all_ppl_name_starting_w_m = deque(inn.strip().split('\n'))
        queue = fuck_all_ppl_name_starting_w_m
        total_fuck_matts_to_give = 0
        while queue:
            current = queue.popleft()
            l, l_val, l_max = 0, "", 0
            for i in range(len(current)-1): # -1 not include final number.
                if int(current[i]) > l_max:
                    l, l_val, l_max = i, current[i], int(current[i])
            r, r_val, r_max = 0, "", 0
            for i in range(l+1, len(current)): # bounded by l_index.
                if int(current[i]) > r_max:
                    r, r_val, r_max = i, current[i], int(current[i])
            joltage = int(l_val + r_val)
            total_fuck_matts_to_give += joltage
        return total_fuck_matts_to_give

    # (48 min)
    def part2(self, inn: str):
        # brainstorm: instead of above brute force, lest try inverse;
        # this time we know we have 1-9 numbers and the constraint 
        # of 12 DIGITS to form largest number is actually helpful. Create map of k,v 
        # where k = 9, v = list of indices in order
        fuck_all_ppl_name_starting_w_m = deque(inn.strip().split('\n'))
        queue = fuck_all_ppl_name_starting_w_m
        total_fuck_matts_to_give = 0
        while queue:
            # there needs to be at least X digits to the right of the leftbound
            # ie edge: 1 number must have 11 digits to right of it
            # 2nd number must have 10 optional digits to right of it
            # start at 9, find farthest 9 to left
            # then start at 8, bounded by left number find lowest index with 10 digits to right
            # if nothing (no 8s available), then start next number
            current = queue.popleft()
            # make map
            for i in range(9, 0, -1):
                indices = [] # get all indices that are specific number (9)
                for index, x in enumerate(current):
                    if int(x) == i:
                        indices.append(index)
                self.nums[str(i)] = indices
            joltage = ""
            seen = set()
            pos = -1
            joltage = self.recurse(pos, seen, current)


            total_fuck_matts_to_give += int(joltage)
        return total_fuck_matts_to_give
            
    def recurse(self, pos, seen, current):
        joltage = ""
        for number, indices in self.nums.items():
            # start at 9 and work down to build our "joltage"
            # we also know our list of indices are ordered.
            if len(seen) == 12:
                break
            for index in indices:
                #  index not already in use, its right of position, we have plenty letters left..
                if index not in seen and pos < index and (len(current) - index) >= (12 - len(seen)):
                    seen.add(index)
                    joltage = number + self.recurse(index, seen, current)
                    break # found best candidate because we know leftmost highest is goal.
        return joltage