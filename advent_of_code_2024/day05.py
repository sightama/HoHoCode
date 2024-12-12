from copy import deepcopy
from collections import deque, defaultdict
from typing import List

DAY = 5


class AdventCode:

    def part1(self, inn: str):
        inn = inn.split('\n')
        total_value = 0
        rules_str = deque()
        updates = deque()
        for row in inn:
            if '' == row:
                continue
            elif '|' in row:
                rules_str.append(row)
            elif ',' in row:
                updates.append(row)

        rules = deque()  # cant use dict same key values. use deque
        for rule in rules_str:
            sl = rule.split('|')
            l, r = sl[0], sl[1]
            rules.append((l, r))

        while updates:
            current = updates.popleft()
            current = current.split(',')
            valid = self.check_rules(current, deepcopy(rules))
            if valid:
                mid_indice = len(current)//2
                total_value += int(current[mid_indice])  # middle element of list/deque

        return total_value

        # first parse "rules", and also the "updates"
        # check all rules against each line. two counters, each update is short/finite. sliding window left|rght
        # if all rules pass, get middle value and add to total_valuee
        # return total value

    @staticmethod
    def check_rules(update: List, rules: deque):
        while rules:
            l, r = rules.popleft()
            order = []
            for x in update:
                if x == l:
                    order.append('l')
                if x == r:
                    order.append('r')
            if len(order) == 0 or len(order) == 1:
                continue
            if order[0] == 'r' and order[1] == 'l':
                return False
        return True
