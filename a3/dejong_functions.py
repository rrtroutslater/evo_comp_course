import numpy as np
from util import *
# dejong functions 1-4

class DejongFitnessFunction(object):
    def __init__(
            self,
            id,
            n_bits=15,
        ):
        
        assert id in [1,2,3,4]
        self.id = id

        self.expected_bitshapes = {
            1 : (3, n_bits),
            2 : (2, 20), # TODO
            3 : (2, 20), # TODO
            4 : (2, 20), # TODO
        }

        self.fitness_functions = {
            1 : dejong_1,
            # TODO - the rest of the dejong functions 
        }

        self.pop_shape = self.expected_bitshapes[self.id]
        self.fitness_function = self.fitness_functions[self.id]
        return

    def evaluate_fitness(
            self,
            population,
        ):
        """
        input:
            - population : a population object of appropriate dimensions for the 
            corresponding dejong function

        returns:
            - fitness as calculated by the dejong function for the population
        """
        pop = population.p.reshape(
            population.p.shape[0], self.pop_shape[0], self.pop_shape[1]
            )
        return self.fitness_function(pop)
   

def dejong_1(x):
    """ 
    dejong function 1: sum_i=1^3 (x_i)^2
    inputs:
        x : bit binary numpy array of shape (num_pop, 3, n_bits)
    returns:
        numpy array of shape (num_pop, ) of fitness values
    """
    assert len(x.shape) == 3
    assert x.shape[1] == 3

    max_fitness = 3 * (5.12)**2

    x_d = np.zeros(shape=(x.shape[0], x.shape[1]))
    i = 0
    for p in x:
        x_d[i] = bin_to_dec(p, -5.12, 5.12)
        i += 1
    # print('X SHAPE:\t', x.shape)
    # print(x_d)

    fitness = np.sum(np.multiply(x_d[:], x_d[:]), axis=1)
    return fitness

def dejong_2(x):
    """
    """



    return

