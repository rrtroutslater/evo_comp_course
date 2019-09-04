from State_2 import * 
from Graph import Graph

def build_graph_start_finish(start, goal, shortest_path=[]):
    # print('start state:\n', start)
    g = Graph()
    state_q = []
    g.add_vertex(start)
    state_q.append([start,[]])

    current_state = start 
    while current_state != goal:
        valid_acts = current_state.get_valid_acts()
        # print('current state:')
        # print(current_state)
        # print('valid acts:\t', valid_acts)
        if len(valid_acts) > 0:
            next_possible_states = current_state.apply_acts(valid_acts)
            for s in next_possible_states:
                # print('considering state:\n', s)
                if g.add_edge([current_state, s]):
                    # print('added edge between above and current')
                    state_q.append([s, current_state])
                # else:
                    # print('above and current represents duplicate edge.. NOT ADDED')
                # input("Press Enter to continue...")
        # print(len(g.edges))
        current_state = state_q[0][0]
        previous_state = state_q[0][1]
        state_q.pop(0)
        if current_state == goal:
            shortest_path.append(goal)
            print('goal state reached:\n', current_state)

    if start == goal:
        shortest_path.append(start)
        return shortest_path
    else:
        return build_graph_start_finish(start, previous_state, shortest_path)
    # return shortest_path

"""
append [s, previous_s] to state q
when goal state is reached:
shortest_path.append(goal=state_q[0][0])
shortest_path.append(previous = state_q[0][1])

then call build_graph_start_finish(start, previous_state)
until start == goal 

reverse shortest_path
print shortest_path
"""


def main():
    start = State()
    goal = State(boat_bank='r', num_l=np.array([0,0]), num_r=np.array([3,3]))
    sp = build_graph_start_finish(start, goal)
    print(sp)
    for s in sp:
        print(s)

    # for i in range(0, len(sp.reverse())):
    #     print(sp[i])


if __name__ == "__main__":
    main()
    pass

