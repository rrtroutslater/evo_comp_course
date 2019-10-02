from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 
from dejong_functions import *
from population import *
from ga import *

def main():
    n_max_iter = 50
    pop_size = 100
    n_runs = 30
    mutation_prob = 0.001
    crossover_prob = 0.7

    # # de jong 1
    # ga = GeneticAlg(
    #     pop_size, 
    #     1,
    #     mutation_prob=mutation_prob,
    #     crossover_prob=crossover_prob,
    #     n_bits=10
    # )
    # ga.run_ga(
    #     num_generation=n_max_iter,
    #     num_run=n_runs,
    #     verbose=True,
    #     plot_results=True
    # )

    # # de jong 2
    # ga = GeneticAlg(
    #     pop_size, 
    #     2,
    #     mutation_prob=mutation_prob,
    #     crossover_prob=crossover_prob,
    #     n_bits=12
    # )
    # ga.run_ga(
    #     num_generation=n_max_iter,
    #     num_run=n_runs,
    #     verbose=True,
    #     plot_results=True
    # )

    # de jong 3
    # ga = GeneticAlg(
    #     pop_size, 
    #     3,
    #     mutation_prob=mutation_prob,
    #     crossover_prob=crossover_prob,
    #     n_bits=10
    # )
    # ga.run_ga(
    #     num_generation=n_max_iter,
    #     num_run=n_runs,
    #     verbose=True,
    #     plot_results=True
    # )

    # de jong 4
    dj4_max_fit = calc_dejong_4_max()
    # print(dj4_max_fit)
    ga = GeneticAlg(
        pop_size, 
        4,
        mutation_prob=mutation_prob,
        crossover_prob=crossover_prob,
        n_bits=8
    )
    ga.run_ga(
        num_generation=n_max_iter,
        num_run=n_runs,
        verbose=True,
        plot_results=True
    )
    return


if __name__ == "__main__":
    main()
    pass