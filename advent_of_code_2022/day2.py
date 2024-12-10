from collections import deque
from advent_of_code.utils import read_input_file
class adventOfCode:
    action_values = {'X': 1,  # rock
                     'A': 1,
                     'Y': 2,  # paper
                     'B': 2,
                     'Z': 3,  # scissor
                     'C': 3}
    action_map = {'X': 'rock',  # rock
                  'A': 'rock',
                  'Y': 'paper',  # paper
                  'B': 'paper',
                  'Z': 'scissor',  # scissor
                  'C': 'scissor'}
    encrypt = {'X': 'l',
               'Y': 'd',
               'Z': 'w'}
    another_map = {'w': 6,
                   'l': 0,
                   'd': 3}

    def part1(self, actions):
        actions = actions.strip()
        rounds = actions.split('\n')
        rounds = [x.strip() for x in rounds]
        total_pts = 0
        for round in rounds:
            options = round.split(' ')
            score = self.compare(options[0], options[1])
            total_pts += score

        return total_pts

    def compare(self, enemy, me):
        result = 0
        enemy_act = self.action_map[enemy]
        me_act = self.action_map[me]

        if enemy_act == me_act:
            result = self.another_map['d'] + self.action_values[me]
        elif enemy_act == 'rock' and me_act == 'paper':
            result = self.another_map['w'] + self.action_values[me]
        elif enemy_act == 'paper' and me_act == 'scissor':
            result = self.another_map['w'] + self.action_values[me]
        elif enemy_act == 'scissor' and me_act == 'rock':
            result = self.another_map['w'] + self.action_values[me]
        else:
            result = self.another_map['l'] + self.action_values[me]

        return result

    def part2(self, actions):
        actions = actions.strip()
        rounds = actions.split('\n')
        rounds = [x.strip() for x in rounds]
        total_pts = 0
        for round in rounds:
            options = round.split(' ')
            score = self.compare_p2(options[0], options[1])
            total_pts += score

        return total_pts

    def compare_p2(self, enemy, me):
        result = 0
        enemy_act = self.action_map[enemy]
        # me_act = self.action_map[me]

        if enemy_act == 'rock':
            if self.encrypt[me] == 'l':
                result = self.another_map['l'] + self.action_values['C']
            elif self.encrypt[me] == 'w':
                result = self.another_map['w'] + self.action_values['B']
            elif self.encrypt[me] == 'd':
                result = self.another_map['d'] + self.action_values[enemy]

        elif enemy_act == 'paper':
            if self.encrypt[me] == 'l':
                result = self.another_map['l'] + self.action_values['A']
            elif self.encrypt[me] == 'w':
                result = self.another_map['w'] + self.action_values['C']
            elif self.encrypt[me] == 'd':
                result = self.another_map['d'] + self.action_values[enemy]

        elif enemy_act == 'scissor':
            if self.encrypt[me] == 'l':
                result = self.another_map['l'] + self.action_values['B']
            elif self.encrypt[me] == 'w':
                result = self.another_map['w'] + self.action_values['A']
            elif self.encrypt[me] == 'd':
                result = self.another_map['d'] + self.action_values[enemy]

        return result





if __name__ == "__main__":
    # https://adventofcode.com/2022/day/2
    test = adventOfCode()
    actions_input = \
        """
        A Y
        B X
        C Z
        """
    # answer = test.part2(actions_input)
    actual_data = read_input_file("./inputs/day2.txt")
    answer = test.part2(actual_data)
    print(answer)

