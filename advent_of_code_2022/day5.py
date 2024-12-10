from collections import deque, Counter
from advent_of_code_2022.utils import read_input_file
from string import ascii_lowercase, ascii_uppercase


class AdventOfCode:
    def part1(self, input):
        input = input.split('\n\n', 1)
        stacks, moves = input[0], input[1]
        # make stacks
        stacks = self.make_stacks(stacks)
        result = self.move_shit(moves, stacks)
        # pop top of results
        return result

    def part2(self, input):
        input = input.split('\n\n', 1)
        stacks, moves = input[0], input[1]
        # make stacks
        stacks = self.make_stacks(stacks)
        result = self.move_shit_p2(moves, stacks)
        # pop top of results
        return result


    def make_stacks(self, inputs):
        columns = int(inputs.strip()[-1])
        keklmao = {}
        for x in range(1, columns+1):
            keklmao[x] = []
        inputs = inputs.split('\n')
        inputs = [x for x in inputs if x]
        for row in inputs[-2::-1]:
            kek = row.split(' ')
            column = 1
            space_count = 0
            for k in kek:
                if k == '':
                    space_count += 1
                    if space_count == 4:
                        column += 1
                        space_count = 0
                    continue
                else:
                    keklmao[column].append(k[1])
                    column += 1

        return keklmao

    def move_shit(self, moves, stacks):
        moves = moves.strip().split('\n')
        for move in moves:
            move = move.split(' ')
            how_many = int(move[1])
            remove_from = int(move[3])
            destination = int(move[5])
            # ACTION
            for x in range(how_many):
                my_guy = stacks[remove_from].pop()
                stacks[destination].append(my_guy)

        columns = len(stacks)
        final_result = ''
        for x in range(1, columns+1):
            first_element = str(stacks[x][-1])
            final_result += first_element
        return final_result

    def move_shit_p2(self, moves, stacks):
        moves = moves.strip().split('\n')
        for move in moves:
            move = move.split(' ')
            how_many = int(move[1])
            remove_from = int(move[3])
            destination = int(move[5])
            # ACTION
            hoes = []
            for x in range(how_many):
                my_guy = stacks[remove_from].pop()
                hoes.append(my_guy)

            while hoes:
                current = hoes.pop()
                stacks[destination].append(current)

        columns = len(stacks)
        final_result = ''
        for x in range(1, columns+1):
            first_element = str(stacks[x][-1])
            final_result += first_element
        return final_result


if __name__ == "__main__":
    # https://adventofcode.com/2022/day/5 - p1 20 minutes, lil mistakes such as using str not int comaprator
    # p2 = 10 minutes
    test = AdventOfCode()
    actions_input = \
"""
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
    # answer = test.part1(actions_input)
    # print(answer)

    # actual_data = read_input_file("./inputs/day5.txt")
    # answer = test.part1(actual_data)
    # print(answer)

    ###### PART TWO ######

    # actions_input = \
    #     """
    #     2-4,6-8
    #     2-3,4-5
    #     5-7,7-9
    #     2-8,3-7
    #     6-6,4-6
    #     2-6,4-8
    #     """
    # answer = test.part2(actions_input)
    # print(answer)

    actual_data = read_input_file("./inputs/day5.txt")
    answer = test.part2(actual_data)
    print(answer)
