from __future__ import print_function
import numpy as np 
from dejong_functions import *
from population import *
# from util import *

class GeneticAlg(object):
    def __init__(self,
            num_individual,
            dejong_function,
            mutation_prob=0.001,
            crossover_prob=0.7,
            n_bits=15,
        ):

        self.function = DejongFitnessFunction(dejong_function, n_bits=n_bits)
        self.population = Population(
            num_individual, 
            self.function.pop_shape[0] * self.function.pop_shape[1],
            mutation_prob=mutation_prob,
            crossover_prob=crossover_prob,            
        )
        return

    def run_ga(
            self,
            num_max_iter=5000,
        ):
        """
        inputs:
            - num_max_iter : number of iterations/population update steps to run

        return:
            - numpy arrays of average, minimum, and maximum population fitnesses
            over the population's evolution
        """
        avg_arr = np.zeros(shape=(num_max_iter,))
        min_arr = np.zeros(shape=(num_max_iter,))
        max_arr = np.zeros(shape=(num_max_iter,))

        for i in range(0, num_max_iter):
            # evaluate fitness for current population
            fitnesses = self.function.evaluate_fitness(self.population)

            # run the GA steps
            # fitness proportional selection
            self.population.fitness_proportional_selection(fitnesses)
            # mutation 
            self.population.mutate()
            # crossover
            self.population.single_crossover()

            # log the statistics 
            avg_arr[i], min_arr[i], max_arr[i] = self.calc_fitness_stats(fitnesses)
        return avg_arr, min_arr, max_arr

    def calc_fitness_stats(
            self, 
            fitnesses
        ):
        # TODO: calculate min, max, average fitness for current population state
        max_fit = np.max(fitnesses)
        min_fit = np.min(fitnesses)
        avg_fit = np.average(fitnesses)
        return avg_fit, min_fit, max_fit












