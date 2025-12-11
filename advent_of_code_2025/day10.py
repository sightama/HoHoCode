from collections import deque, Counter
from functools import cache
from copy import deepcopy, copy
import sys

DAY = 10
"""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

class AdventCode:
    
    # x time
    def part1(self, inn: str):
        # goal - find fewest button press to reach state, add all up
        inn = inn.split('\n')
        states = []
        buttons = []
        for x in inn:
            # get buttons and states to find
            all_parts = x.split(' ')
            states.append(all_parts[0])
            buttons.append(all_parts[1:-1])
        
        all_final_vals = []
        for state, butts in zip(states, buttons):
            # now get lowest button presses all variations until lowest. also stop iterating past lowest num if already there.
            lights = [False] * (len(state) - 2)
            goal_state, i = deepcopy(lights), 0
            indices = []
            for char in state:  # create ideal state lights.
                if char in ['[', ']']:
                    continue
                if char == '#':
                    goal_state[i] = not goal_state[i]
                    indices.append(i)
                i += 1
            
            # try all cases where the actual indices that are true are the primary numbers inside tuples.
            # theory: If there are TWO on lights,
            # lets order such that buttons that have are numbers are tried first.
            ordered_buttons = butts
            # ordered_buttons = []
            # the_rest = []
            # for butt in butts:
            #     if any(str(x) in butt for x in indices):
            #         ordered_buttons.append(butt)
            #     else:
            #         the_rest.append(butt)
            # ordered_buttons.extend(the_rest)

            lowest = None
            queue = deque([(0, deepcopy(lights), set())])
            # now try all variations, automatically shortest path if any single button causes perfect state stop.
            while queue:
                steps, prev_state, seen = queue.popleft()
                # append all next states to try; add all variations minus our number
                for butts in ordered_buttons:
                    if butts in seen:
                        continue
                    # try this button with all x1 to see all cases where just press 2 buttons, then three then 4 buttons etc.
                    current_state = self.change_state(deepcopy(prev_state), butts)

                    if current_state == goal_state:
                        lowest = steps + 1
                        break  # by how we are doing this first time we hit it thats the lowest num of steps.
                    else:
                        queue.append((steps + 1, deepcopy(current_state), seen.union(set([butts]))))  # now + 1 steps, attempt all permutation with this button.
                if lowest is not None:
                    break
        
            all_final_vals.append(lowest)
            print(f"Running sum is {sum(all_final_vals)}")
        return sum(all_final_vals)

    @cache
    def splitt(self, buttons):
        buttons = buttons[1:-1]
        buttons = buttons.split(',')
        return buttons


    def change_state(self, state, buttons):
        buttons = self.splitt(buttons)
        for button in buttons:
            state[int(button)] = not state[int(button)]
        return state


        

        