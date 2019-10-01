from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 
from dejong_functions import *
# from util import *
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
    
    n_bits = 10
    n_max_iter = 100
    pop_size = 50
    n_runs = 30
    mutation_prob = 0.001
    crossover_prob = 0.7

    # de jong 1
    ga = GeneticAlg(
        pop_size, 
        1,
        mutation_prob=mutation_prob,
        crossover_prob=crossover_prob,
        n_bits=10
    )
    ga.run_ga(
        num_generation=n_max_iter,
        num_run=n_runs,
        verbose=True,
        plot_results=True
    )

    # de jong 2
    # ga = GeneticAlg(
    #     pop_size, 
    #     2,
    #     mutation_prob=mutation_prob,
    #     crossover_prob=crossover_prob,
    #     n_bits=12
    # )
    # ga.run_ga(
    #     num_max_iter=n_max_iter,
    #     num_run=n_runs,
    #     verbose=True,
    #     plot_results=True
    # )


    # de jong 2
    # ga = GeneticAlg(
    #     pop_size, 
    #     2,
    #     mutation_prob=mutation_prob,
    #     crossover_prob=crossover_prob,
    #     n_bits=12
    # )

    # avg_arr = np.zeros(shape=(n_max_iter,))
    # min_arr = np.zeros(shape=(n_max_iter,))
    # max_arr = np.zeros(shape=(n_max_iter,))

    # for i in range(0, n_runs):
    #     # ga = GeneticAlg(pop_size, 1, # de jong 1
    #     ga = GeneticAlg(pop_size, 2, # de jong 2
    #         mutation_prob=mutation_prob,
    #         crossover_prob=crossover_prob,
    #         n_bits=n_bits
    #     )
    #     x, y, z = ga.run_ga(num_max_iter=n_max_iter)
    #     avg_arr += x 
    #     min_arr += y
    #     max_arr += z

    # # de jong 1
    # # max_fit = np.ones_like(avg_arr) * 3 * (5.12**2)
    # # de jong 2
    # x1_max = -2.048
    # x2_max = -2.048
    # max_fit = np.ones_like(avg_arr) * 100 * (x1_max**2 - x2_max)**2 + (1 - x1_max)**2
    # print(max_fit)

    # plt.plot(max_fit, label='limit', linestyle='--')
    # plt.plot(avg_arr/n_runs, label='avg')
    # plt.plot(min_arr/n_runs, label='min')
    # plt.plot(max_arr/n_runs, label='max')
    # plt.legend(loc='lower right')
    # plt.title(s="pX = " + str(crossover_prob) + ", pM = " + str(mutation_prob))
    # # plt.ylim((0,100))   # 1
    # plt.ylim((0,4200))  # 2
    # plt.show()
    return


if __name__ == "__main__":
    main()
    pass