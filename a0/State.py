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
        assert boat_capacity in [2,3]
        if boat_capacity == 2:
            self.possible_actions = np.array(
                [[1,0], [0,1], [1,1], [2,0], [0,2]]
                )
        elif boat_capacity == 3:
            self.possible_actions = np.array(
                # [1,2] is not allowable
                [[1,0], [0,1], [1,1], [2,0], [0,2], [2,1], [3,0], [0,3]]
                )
        # num_l/r = [m,c], where m = # of missionary, c = # of cannibal
        self.state = {'bank':boat_bank, 'l':num_l, 'r':num_r}
        self.boat_capacity = boat_capacity
        return

    def get_valid_acts(self):
        """ 
        returns a list of numpy arrays of all valid actions
        """
        valid_acts = []
        b = self.state['bank']
        for act in self.possible_actions:
            # checking current bank 
            new_num = self.state[b] - act
            current_bank_ok = False
            if (new_num[0] >= new_num[1] or new_num[0] == 0)\
                    and new_num[0] >= 0 and new_num[1] >= 0:
                current_bank_ok = True

            # checking next bank 
            next_b = 'l' if b == 'r' else 'r'
            new_num = self.state[next_b] + act 
            next_bank_ok = False
            if (new_num[0] >= new_num[1] or new_num[0] == 0)\
                    and new_num[0] <= 3 and new_num[1] <= 3:
                next_bank_ok = True

            if current_bank_ok and next_bank_ok:
                valid_acts.append(act)
        return valid_acts

    def apply_acts(self, valid_acts):
        """ 
        given valid actions, returns list of accessable states  
        """
        valid_states = []
        for act in valid_acts:
            valid_states.append(self.apply_act(act))
        return valid_states

    def apply_act(self, act):
        """
        applies a single action to current state, returns a new state
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
            boat_capacity=self.boat_capacity,
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

