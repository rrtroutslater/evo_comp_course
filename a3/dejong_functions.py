import numpy as np
from util import *
# dejong functions 1-4


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

    x_d = np.zeros(shape=(x.shape[0]))
    for p in x:
        x_d = bin_to_dec(p, -5.12, 5.12)

    fitness = np.zeros(shape=x.shape[0])
    fitness[:] = np.sum(np.multiply(x_d[:], x_d[:]))
    # print(fitness.shape)
    # print(fitness)
    return fitness


