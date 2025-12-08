from collections import deque, Counter
from copy import deepcopy

DAY = 6


class AdventCode:

    @staticmethod  # took 15 min
    def part1(inn: str):
        result = 0
        grid = inn.strip().split('\n')
        operations = grid[-1]
        grid.remove(operations)
        operations = [x for x in operations if not x.isspace()]
        new_grid = []
        for nums in grid:
            row = nums.split(' ')
            row = [int(x) for x in row if x.isdigit()]
            new_grid.append(row)
        for x in range(len(new_grid[0])):
            nums = []  # start first row x = 0 for all y's
            for y in range(len(new_grid)):
                nums.append(new_grid[y][x])
            if operations[x] == '*':
                final = 1
                for i in nums:
                    final *= i
            if operations[x] == '+':
                final = 0
                for i in nums:
                    final += i
            result += final
        return result


    # new things: Start at grid[0] (top) and go down
    # We know that you find the longest nums (len(num) == 3), get all nums that are 3 digits, go top to bottom.
    # nevermind fuck trying above, its all whitespace movement.

    # idea: Find the EXACT X pos of the operators. This represents where we END every calculation.
    # To find the STARTING X point we go up and down on each char until we find the ONLY WHITESPACE column.
    # From there we go, for every X-1, start at y==0 and do y+1 and check if ' ' skip, if not append y[i]. 
    # at end do operator logic. seems simple eh?
    # took 1 hour 10 minutes
    @staticmethod
    def part2(inn: str):
        grid = inn.strip().split('\n')
        operations = grid[-1]
        grid.remove(operations)
        
        operation_locations = [] # find operation locations (ie the "starting points")
        for i, char in enumerate(operations):
            if char in ['*', '+']:
                operation_locations.append((i, char))
        final_op = operation_locations.pop()  # no whitespace column for last equation.
        endpoints = []
        for x, char in operation_locations:  # the starting points, go right find where all whitespace.
            all_white = True
            final_x = x+1 # +1 we dont count the starting point, thats clearly not whitespace.
            while all_white:
                for y in range(len(grid)):
                    if grid[y][final_x] != ' ':
                        all_white = False
                        break
                if all_white:
                    endpoints.append(final_x)
                    break
                else:  # This column WAS NOT our final column. try again on next.
                    all_white = True
                    final_x = final_x + 1
        # edge case: There is no whitespace for the final column? What do? I think just append lenx,leny to end (4 start 3 stops + length)
        endpoints.append(len(grid[0]))  # not -1 because we subtract -1 for whitespace from all.
        operation_locations.append(final_op)
        x_cases = deque()
        for tupl, end_x in zip(operation_locations, endpoints):
            x, char = tupl
            x_cases.append((x, end_x, char))
        total = 0
        # NOW we do each equation and compute on-the-fly
        while x_cases:
            all_values_for_op = []
            start, end, op = x_cases.popleft()
            end -= 1 # to account for whitespace column,
            while end != start - 1:
                num = ''
                for y in range(len(grid)):
                    if grid[y][end] == ' ':
                        continue
                    else:
                        num = num + grid[y][end]
                if num and not num.isspace():
                    all_values_for_op.append(int(num))
                end -= 1
            # we have our nums, now do op.
            if op == '*':
                subtotal = 1
                for num in all_values_for_op:
                    subtotal *= num
            if op == '+':
                subtotal = 0
                for num in all_values_for_op:
                    subtotal += num
            total += subtotal
        return total
