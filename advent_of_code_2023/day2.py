from collections import deque


class AdventCode:

    @staticmethod
    def part1(inn: str, red, green, blue):
        maxes = {'red': red, 'green': green, 'blue': blue}
        possibles = []
        inn = inn.strip()
        lines = inn.split('\n')
        for line in lines:
            possible = True
            flavors = line.split(':')
            idd = flavors[0].split(' ')[1]
            rounds = flavors[1].split(';')
            for round in rounds:
                if not possible:
                    break
                round_of_cubes = round.split(',')
                for cubes in round_of_cubes:
                    test = cubes.strip().split(' ')
                    how_many = int(test[0])
                    color = test[1]
                    if how_many > maxes[color]:
                        possible = False
                        break
            if possible:
                possibles.append(int(idd))

        return sum(possibles)


    @staticmethod
    def part2(inn: str):
        powers = []
        inn = inn.strip()
        lines = inn.split('\n')
        for line in lines:
            mins = {'red': -1e99, 'green': -1e99, 'blue': -1e99}
            flavors = line.split(':')
            idd = flavors[0].split(' ')[1]
            rounds = flavors[1].split(';')
            for round in rounds:
                round_of_cubes = round.split(',')
                for cubes in round_of_cubes:
                    test = cubes.strip().split(' ')
                    how_many = int(test[0])
                    color = test[1]
                    if how_many > mins[color]:
                        mins[color] = how_many

            vals = list(mins.values())
            result = 1
            for val in vals:
                result *= val
            powers.append(result)

        return sum(powers)