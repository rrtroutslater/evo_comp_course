from __future__ import print_function
import numpy as np 
from State import *

""" 
cannibals, missionaries

state:

"""

class Graph(object):
    def __init__(self):
        self.vertices = []
        self.edges = []

    def add_vertex(self, new_v):
        if len(self.vertices) == 0:
            self.vertices.append(new_v)
            return True
        i = 0
        while i < len(self.vertices):
            if self.vertices[i] == new_v:
                return False
            i += 1
        self.vertices.append(new_v)
        return True

    def add_edge(self, new_e):
        if new_e not in self.edges:# and new_e.reverse() not in self.edges:
            self.edges.append(new_e)
            # self.edges.append(new_e.reverse())
            return True
        return False


def build_graph(start):
    return


def find_path_bfs(start, goal):
    """
    find a path from start to goal (if there is one) using breadth first search
    """
    state_q = []
    states_visited = []
    g = Graph()
    g.add_vertex(start)
    # g.add_vertex(goal)
    # append new states to end
    # start search at position 0, 

    current_state = start 
    while current_state != goal:
        next_states = current_state.get_possible_next_states()
        print(next_states)
        for s in next_states:
            # if s.is_valid:# and not s in states_visited:# and not s in state_q:
            # # new state must be valid, and correspond to new vertex or new edge
            print(s.is_valid)
            print(len(g.edges))
            if g.add_edge([current_state, s]):
                state_q.append(s)
                # states_visited.append(s)
        print(len(state_q))
        current_state = state_q[0]
        state_q.pop(0)
        # print(len(g.vertices))
        print('\ncurrent state:')
        print(current_state)

    return 


def main():
    s = State()
    goal_state = State(
        boat_bank='r', num_l=np.array([0,0]), num_r=np.array([3,3]), boat_capacity=1
        )

    print(s)
    print(goal_state)

    print("-------------------------------------------------")
    find_path_bfs(s, goal_state)

    return


if __name__ == "__main__":
    main()

