import numpy as np
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
            2 : (2, 12),
            3 : (2, 20), # TODO
            4 : (2, 20), # TODO
        }

        self.fitness_functions = {
            1 : dejong_1,
            2 : dejong_2,
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

    x_d = bin_arr_to_dec_arr(x, -5.12, 5.12)
    fitness = max_fitness - np.sum(np.multiply(x_d[:], x_d[:]), axis=1)
    # best_idx = np.argmax(fitness)
    # print('best fitness:\t', fitness[best_idx])
    # print(x[best_idx])
    # print(bin_to_dec(x[best_idx], -5.12, 5.12))
    # print(bin_to_dec(x[best_idx], -5.12, 5.12) > max_fitness)
    return fitness

def dejong_2(x):
    """
    dejong function 2: 100 * (x1^2 - x2)^2 + (1-x1)^2
    """
    assert len(x.shape) == 3
    assert x.shape[1] == 2

    x1_max = -2.048
    x2_max = -2.048
    max_fitness = 100 * (x1_max**2 - x2_max)**2 + (1 - x1_max)**2

    x_d = bin_arr_to_dec_arr(x, -2.048, 2.048)

    fitness = np.zeros(shape=(x.shape[0],))
    i = 0
    for num_arr in x_d:
        fitness[i] = 100 * (num_arr[0]**2 - num_arr[1])**2 + (1 - num_arr[0])**2
        i += 1
    # best_idx = np.argmax(fitness)
    # print('best fitness:\t', fitness[best_idx])
    # print(x[best_idx])
    # print(bin_to_dec(x[best_idx], -2.048, 2.048))
    # print(bin_to_dec(x[best_idx], -2.048, 2.048) > max_fitness)
    return fitness

def dejong_3(x):
    """
    """
    return

def bin_arr_to_dec_arr(x, n_min, n_max):
    x_d = np.zeros(shape=(x.shape[0], x.shape[1]))
    i = 0
    for p in x:
        x_d[i] = bin_to_dec(p, n_min, n_max)
        i += 1
    return x_d

def bin_to_dec(n_b, n_min, n_max):
    """
    n_b : (N, num_bits) binary numpy array
    n_min : minimum value of decimal range
    n_max : maximum value of decimal range

    returns : numpy arra of decimal numbers in [n_min, n_max)
    """
    n_bits = n_b.shape[1]
    n_d = np.zeros(shape=(n_b.shape[0],))
    for i in range(0, n_b.shape[1]):
        n_d[:] += (2**(n_bits - i - 1)) * n_b[:,i]
    n_d[:] *= (n_max - n_min) / (2**n_b.shape[1])
    n_d += n_min
    return n_d