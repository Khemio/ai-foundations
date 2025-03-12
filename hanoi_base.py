import math
from search import Problem


class Hanoi(Problem):
    def __init__(self):
        # super().__init__(write initial state here, [write goal states here])
        super().__init__([{1,2,3}, set(), set()], [[set(), set(), {1,2,3}]])
        # pass

    def actions(self, state):
        acts = []
        inf_set = {math.inf}

        # Calculate possible actions here
        for i in range(3):
            for j in range(3):
                if i != j:
                    for k in range(1,4):
                        if k == min(state[i].union(inf_set)) and k < min(state[j].union(inf_set)):
                            acts.append("o {} {} {}".format(i + 1, j + 1, k))

        return acts

    def actions2(self):
        acts = []
        temp_acts = []
        new_states = []
        inf_set = {math.inf}
        cur_state = self.initial

        temp_acts = self.actions(cur_state)

        print("State 1: {}".format(cur_state))
        print("Actions 1: {}".format(temp_acts))

        # print()

        for n in range(len(temp_acts)):
            print()
            # print("Current: {}".format(cur_state))
            temp_state = self.result(cur_state, temp_acts[n])
            print("State 2.{}: {}".format(n+1, temp_state))
            new_states.append(temp_state)
            # temp_acts = self.actions(temp_state)
            acts.append(self.actions(temp_state))
            print("Actions 2.{}: {}".format(n+1,acts[n]))


        # print("New states: {}".format(new_states))

        # return acts

    def result(self, state, action):
        i, j, k = action.split(' ')[1:]
        i, j, k = int(i), int(j), int(k)

        new_state = state.copy()

        # print("State: {}".format(state))

        for l in range(1,4):
            if l == j:
                new_state[l - 1] = state[l - 1].union({k})
            else:
                new_state[l - 1] = state[l - 1].difference({k})

        # print("State: {}".format(state))
        # print("New state: {}".format(new_state))

        # calculate and return new state here
        return new_state


def main():
    h = Hanoi()

    # Test if actions works correctly
    # print(h.actions([{1, 2, 3}, set(), set()]))
    # print(h.actions([{1}, {2, 3}, set()]))

    # Test if result works correctly
    # print(h.result(
    # state=[{1}, {2,3}, set()],
    # action="o 2 3 2"
    # ))

    # print(h.result(
    # state=[{1,2,3}, set(), set()],
    # action="o 1 3 1"
    # ))

    # print(h.actions2())
    h.actions2()


main()
