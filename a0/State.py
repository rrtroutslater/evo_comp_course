import numpy as np 

class State(object):
    def __init__(
            self,
            boat_bank='l',
            num_l=np.array([3,3]),
            num_r=np.array([0,0]),
            num_b=0,
            boat_capacity=2,
            ):

        self.possible_actions = np.array([[1,0], [0,1], [1,1], [2,0], [0,2]])
        self.state = {'bank':boat_bank, 'l':num_l, 'r':num_r}
        self.boat_capacity = boat_capacity
        return

    def get_valid_acts(self):
        """ 
        returns a list of numpy arrays of all actions which leave current bank 
        in valid state
        """
        valid_acts = []
        b = self.state['bank']
        for act in self.possible_actions:
            new_num = self.state[b] - act
            # num miss > num can, all num >= 0
            if new_num[0] >= new_num[1] and new_num[0] >= 0 and new_num[1] >= 0:
                valid_acts.append(act)
        return valid_acts

    def apply_acts(self, valid_acts):
        """ 
        acts is list of numpy array 
        returns list of visitable states 
        """
        valid_states = []
        for act in valid_acts:
            valid_states.append(self.apply_act(act))
        return valid_states

    def apply_act(self, act):
        """
        applies a single action to current state, 
        returns a new state if new state 
        """
        current_bank = self.state['bank']
        if current_bank == 'l':
            new_bank = 'r'
        else:
            new_bank = 'l'

        new_state = State(
            boat_bank=new_bank,
            num_l= self.state['l']-act if current_bank == 'l' else self.state['l']+act,
            num_r= self.state['r']-act if current_bank == 'r' else self.state['r']+act,
        )
        return new_state

    def __str__(self):
        s = "boat bank:\t{0}\nm, c on left:\t{1}\nm, c on right:\t{2}"\
            .format(self.state['bank'], self.state['l'], self.state['r'],
            )
        return s

    def __eq__(self, s):
        return self.state['bank'] == s.state['bank']\
            and np.array_equal(self.state['l'], s.state['l'])\
            and np.array_equal(self.state['r'], s.state['r'])\


