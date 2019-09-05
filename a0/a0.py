from State import * 
from Graph import Graph

def build_graph_start_finish(start, goal, shortest_path=[]):
    """
    uses BFS to find shortest path from start to goal
    returns a list of the states in the shortest path
    """
    # print('start state:\n', start)
    g = Graph()
    state_q = []
    g.add_vertex(start)
    state_q.append([start,[]])

    current_state = start 
    while current_state != goal:
        valid_acts = current_state.get_valid_acts()
        # print('\nstate queue:')
        # for s in state_q:
        #     print(s[0])
        # print('\ncurrent state:')
        # print(current_state)
        # print('valid acts:\t', valid_acts)
        if len(valid_acts) > 0:
            next_possible_states = current_state.apply_acts(valid_acts)
            for s in next_possible_states:
                # print('considering state:\n', s)
                if g.add_vertex(s):
                    # print('added vertext to graph')
                    state_q.append([s, current_state])
                # else:
                #     print('DUPLICATE VERTEX NOT ADDED')
                # input("Press Enter to continue...")
        state_q.pop(0)
        current_state = state_q[0][0]
        previous_state = state_q[0][1]
        if current_state == goal:
            shortest_path.append(goal)
            # print('goal state reached:\n', current_state)

    if start == goal:
        shortest_path.append(start)
        return shortest_path
    else:
        return build_graph_start_finish(start, previous_state, shortest_path)

def main():
    # 2 passengers
    # print('\n2 passenger case --------')
    # start = State()
    # goal = State(boat_bank='r', num_l=np.array([0,0]), num_r=np.array([3,3]))
    # sp = build_graph_start_finish(start, goal)
    # sp.reverse()
    # for s in sp:
    #     print(s)

    # 3 passengers
    print('\n3 passenger case --------')
    start = State(boat_capacity=3)
    goal = State(boat_bank='r', num_l=np.array([0,0]), 
                num_r=np.array([3,3]), boat_capacity=3)
    sp_3 = build_graph_start_finish(start, goal)
    sp_3.reverse()
    for s in sp_3:
        print(s)

if __name__ == "__main__":
    main()
    pass