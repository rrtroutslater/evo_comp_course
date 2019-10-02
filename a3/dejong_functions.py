import numpy as np

class DejongFitnessFunction(object):
    def __init__(
            self,
            id,
            n_bits=10,
        ):
        
        assert id in [1,2,3,4]
        self.id = id

        self.expected_bitshapes = {
            1 : (3, n_bits),
            2 : (2, n_bits),
            3 : (5, n_bits),
            4 : (30, n_bits), # TODO
        }

        self.fitness_functions = {
            1 : self.dejong_1,
            2 : self.dejong_2,
            3 : self.dejong_3,
            4 : self.dejong_4
        }

        self.input_bounds = {
            1 : [-5.12, 5.12],
            2 : [-2.048, 2.048],
            3 : [-5.12, 5.12],
            4 : [-1.28, 1.28]
        }

        self.pop_shape = self.expected_bitshapes[self.id]
        self.fitness_function = self.fitness_functions[self.id]
        self.bounds = self.input_bounds[self.id]
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

        fitness, max_fitness = self.fitness_function(pop)
        return fitness, max_fitness

    def dejong_1(self, x):
        """ 
        dejong function 1: sum_i=1^3 (x_i)^2
        inputs:
            x : bit binary numpy array of shape (num_pop, 3, n_bits)
        returns:
            numpy array of shape (num_pop, ) of fitness values
        """
        assert len(x.shape) == 3
        assert x.shape[1] == 3

        max_fitness = 3 * ((5.12)**2)
        # max_fitness = 100

        x_d = bin_arr_to_dec_arr(x, self.bounds)

        i = 0
        fitness = np.zeros(shape=(x_d.shape[0],))
        for num_arr in x_d:
            # print(num_arr)
            fitness[i] = num_arr[0]**2 + num_arr[1]**2 + num_arr[2]**2
            i += 1
        fitness = np.ones_like(fitness)*max_fitness - fitness
        return fitness, max_fitness

    def dejong_2(self, x):
        """
        dejong function 2: 100 * (x1^2 - x2)^2 + (1-x1)^2
        """
        assert len(x.shape) == 3
        assert x.shape[1] == 2

        x1_max = -2.048
        x2_max = -2.048
        max_fitness = 100 * (x1_max**2 - x2_max)**2 + (1 - x1_max)**2

        x_d = bin_arr_to_dec_arr(x, self.bounds)

        fitness = np.zeros(shape=(x.shape[0],))
        i = 0
        for num_arr in x_d:
            fitness[i] = 100 * (num_arr[0]**2 - num_arr[1])**2 + (1 - num_arr[0])**2
            i += 1

        fitness = max_fitness - fitness
        return fitness, max_fitness

    def dejong_3(self, x):
        """
        """
        assert len(x.shape) == 3
        assert x.shape[1] == 5

        max_fitness = 50

        x_d = bin_arr_to_dec_arr(x, self.bounds)
        fitness = np.zeros(shape=(x.shape[0],))
        i = 0
        for num_arr in x_d:
            fitness[i] = np.sum(num_arr.astype(np.int))
            i += 1
        fitness = -1 * fitness + 25
        return fitness, max_fitness

    def dejong_4(self, x):
        """
        """
        assert len(x.shape) == 3
        assert x.shape[1] == 30

        x_d = bin_arr_to_dec_arr(x, self.bounds)

        max_fitness = 1250
        
        fitness = np.zeros(shape=(x.shape[0],))
        idx = 0
        for num_arr in x_d:
            s = 0
            for i in range(0, num_arr.shape[0]):
                s += i * num_arr[i]**4
            s += np.random.normal()
            fitness[idx] = s
            idx += 1

        fitness = max_fitness - fitness
        return fitness, max_fitness


def calc_dejong_4_max():
    max_fit = 0
    for i in range(0, 30):
        max_fit += (i+1)*(1.28**4)
    max_fit += 1
    return max_fit

def bin_arr_to_dec_arr(x, bounds):
    # print('x shape:\t', x.shape)
    x_d = np.zeros(shape=(x.shape[0], x.shape[1]))
    n_min = bounds[0]
    n_max = bounds[1]
    i = 0
    for p in x:
        x_d[i] = bin_to_dec(p, n_min, n_max)
        # print(x_d[i])
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