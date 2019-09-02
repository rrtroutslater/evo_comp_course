from __future__ import print_function
import numpy as np 

""" 
cannibals, missionaries

state:



"""

# class Act(object):


#     ret

class State(object):
    def __init__(self,
            boat_bank='l',
            num_l=np.array([3,3]),
            num_r=np.array([0,0]),
            boat_capacity=1,
            ):

        assert boat_bank in ['l', 'r']
        assert num_l.shape == (2,)
        assert num_r.shape == (2,)
        # always assumes num_l[0] = # of missionary
        # always assumes num_l[1] = # of cannibal
        self.boat_bank=boat_bank
        self.counter = {'l':num_l, 'r':num_r}
        self.is_valid = self.is_state_valid()
        self.boat_capacity = boat_capacity

        return

    def is_state_valid(self):
        # number of missionaries must be >= number of cannibals 
        valid = (self.counter['l'][0] >= self.counter['l'][1]\
            and self.counter['r'][0] >= self.counter['r'][1])
        # can have canibals > missionaries if num missionary = 0
        valid = valid or \
            ((self.counter['l'][0] == 0 and self.counter['l'][1] > 0)\
            or (self.counter['r'][0] == 0 and self.counter['r'][1] > 0)) 
        return valid 

    def get_possible_next_states(self):
        """
        returns list of State objects representing possible next states. NOTE: not all
        states will be valid (ie, some will be failure cases), so check State.is_valid
        when determining which states to add to queue later
        
        possible actions, for any given state:
        switch banks (always)
        take c to other bank, or
        take m to other bank, or
        take 0 to other bank
        """
        # get next bank the boat will be at
        if self.boat_bank == 'l':
            next_bank = 'r'
        else:
            next_bank = 'l'

        # list of next possible states
        next_states = []

        # take nobody to other bank, only if there are people to pick up on other bank
        if self.counter[next_bank][0] > 0 or self.counter[next_bank][1] > 0:
            next_states.append(
                State(boat_bank=next_bank, num_l=self.counter['l'], num_r=self.counter['r'])
            )

        # take missionary to other bank, as long as there exist sufficient missionaries
        if self.counter[self.boat_bank][0] > 0:
            if next_bank == 'l':
                new_num_l = self.counter['l'] + np.array([self.boat_capacity,0])
                new_num_r = self.counter['r'] - np.array([self.boat_capacity,0])
            else:
                new_num_r = self.counter['r'] + np.array([self.boat_capacity,0])
                new_num_l = self.counter['l'] - np.array([self.boat_capacity,0])
            next_states.append(
                State(boat_bank=next_bank, num_l=new_num_l, num_r=new_num_r)
            )

        # take cannibal to other bank, as long as there exist sufficient missionaries
        if self.counter[self.boat_bank][1] > 0:
            if next_bank == 'l':
                new_num_l = self.counter['l'] + np.array([0,self.boat_capacity])
                new_num_r = self.counter['r'] - np.array([0,self.boat_capacity])
            else:
                new_num_r = self.counter['r'] + np.array([0,self.boat_capacity])
                new_num_l = self.counter['l'] - np.array([0,self.boat_capacity])
            next_states.append(
                State(boat_bank=next_bank, num_l=new_num_l, num_r=new_num_r)
            )

        # extend here for other action options with a bigger boat

        return next_states

    def __str__(self):
        s = "boat bank:\t{0}\nm on left:\t{1}\nc on left:\t{2}\
            \nm on right:\t{3}\nc on right:\t{4}\nvalid:\t\t{5}"\
            .format(self.boat_bank, self.counter['l'][0], self.counter['l'][1],\
                self.counter['r'][0], self.counter['r'][1], self.is_valid
            )
        return s

    def __eq__(self, s):
        return self.boat_bank == s.boat_bank and self.counter['l'].all() == s.counter['l'].all()\
            and self.counter['r'].all() == s.counter['r'].all()

