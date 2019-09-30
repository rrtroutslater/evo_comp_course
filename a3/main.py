from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 
from dejong_functions import *
from util import *
from population import *
from ga import *



# genetic algorithm class
"""
fitness proportional selection

uniform crossover

random bitwise mutation

must pass a fitness function to eval?

assume that bit strings have length 150

TODO: clean up objects/passthru parameters ... too much goofy stuff happening ...

pass function as argument to genetic alg

pass population as argument to GA

problem kind of solved!

"""

def main():
    # dejong 1
    n_bits = 15
    n_max_iter = 100
    pop_size = 50
    n_runs = 30
    mutation_prob = 0.001
    crossover_prob = 0.7

    avg_arr = np.zeros(shape=(n_max_iter,))
    min_arr = np.zeros(shape=(n_max_iter,))
    max_arr = np.zeros(shape=(n_max_iter,))

    for i in range(0, n_runs):
        ga = GeneticAlg(pop_size, 1, 
            mutation_prob=mutation_prob,
            crossover_prob=crossover_prob,
            n_bits=n_bits
        )
        x, y, z = ga.run_ga(num_max_iter=n_max_iter)
        avg_arr += x 
        min_arr += y
        max_arr += z

    plt.plot(avg_arr/n_runs)
    plt.plot(min_arr/n_runs)
    plt.plot(max_arr/n_runs)
    plt.show()

    # x = np.zeros(shape=(10, 3, n_bits))
    # dejong_1(x)

    # p = Population(10, 3*n_bits)
    # p.mutate()

    return


if __name__ == "__main__":
    main()
    pass