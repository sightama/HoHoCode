from collections import deque, Counter
from advent_of_code.utils import read_input_file
from string import ascii_lowercase, ascii_uppercase

class adventOfCode:
    prio_map = {}

    def generate_prio(self):
        count = 1
        for letter in ascii_lowercase:
            self.prio_map[letter] = count
            count += 1
        for letter in ascii_uppercase:
            self.prio_map[letter] = count
            count += 1


    def part1(self, rucksacks):
        self.generate_prio()
        sum_prio = 0
        rucksacks = rucksacks.strip()
        rucksacks = rucksacks.split('\n')
        rucksacks = [x.strip() for x in rucksacks]
        for sack in rucksacks:
            half = int(len(sack) / 2)
            left, right = sack[:half], sack[half:]
            intersect = set(left) & set(right)
            priority = self.prio_map[intersect.pop()]
            sum_prio += priority
            priority = 0
        return sum_prio

    def part2(self, rucksacks):
        self.generate_prio()
        sum_prio = 0
        rucksacks = rucksacks.strip()
        rucksacks = rucksacks.split('\n')
        rucksacks = [x.strip() for x in rucksacks]
        rucksacks = [x for x in rucksacks if x != '']
        rucksacks = deque(rucksacks)
        while rucksacks:
            p1, p2, p3 = rucksacks.popleft(), rucksacks.popleft(), rucksacks.popleft()
            intersect = set(p1) & set(p2) & set(p3)
            priority = self.prio_map[intersect.pop()]
            sum_prio += priority
            priority = 0
        return sum_prio




if __name__ == "__main__":
    # https://adventofcode.com/2022/day/3 - 18 minutes part1, 15 minutes p2
    test = adventOfCode()
    actions_input = \
        """
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
    # answer = test.part1(actions_input)
    # print(answer)

    # actual_data = read_input_file("./inputs/day3.txt")
    # answer = test.part1(actual_data)
    #print(answer)



    ###### PART TWO ######

    actions_input = \
        """
        vJrwpWtwJgWrhcsFMMfFFhFp
        jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
        PmmdzqPrVvPwwTWBwg
        
        wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
        ttgJtRGJQctTZtZT
        CrZsJsPPZsGzwwsLwLmpwMDw
        """
    # answer = test.part2(actions_input)
    # print(answer)

    actual_data = read_input_file("./inputs/day3.txt")
    answer = test.part2(actual_data)
    print(answer)
