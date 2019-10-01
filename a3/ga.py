from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt
from dejong_functions import *
from population import *
# from util import *

class GeneticAlg(object):
    def __init__(self,
            num_individual,
            dejong_function_id,
            mutation_prob=0.001,
            crossover_prob=0.7,
            n_bits=15,
        ):

        self.function = DejongFitnessFunction(dejong_function_id, n_bits=n_bits)
        self.num_individual = num_individual
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob
        self.population = None
        self.initialize_population()
        return

    def initialize_population(self):
        self.population = Population(
            self.num_individual, 
            self.function.pop_shape[0] * self.function.pop_shape[1],
            mutation_prob=self.mutation_prob,
            crossover_prob=self.crossover_prob,
        )        
        return 

    def run_ga(
            self,
            num_generation=100,
            num_run=30,
            verbose=True,
            plot_results=True,
        ):
        """
        inputs:
            - num_generation : number of iterations/population update steps to run

        return:
            - numpy arrays of average, minimum, and maximum population fitnesses
            over the population's evolution
        """
        avg_arr = np.zeros(shape=(num_generation,))
        min_arr = np.zeros(shape=(num_generation,))
        max_arr = np.zeros(shape=(num_generation,))

        for i in range(0, num_run):
            x, y, z, max_fitness = self.run_ga_optimization(num_generation)
            avg_arr += x 
            min_arr += y 
            max_arr += z
            self.initialize_population()

        if verbose:
            print(np.argmax(z))
            print('example best population member:\n', \
                np.reshape(self.population.p[np.argmax(z)], \
                (self.function.pop_shape[0], self.function.pop_shape[1]))
            )
            print('in decimal:\n', )
            print('corresponding fitness:\t\t\t', np.max(z))
            print('max possible fitness (theoretical):\t', max_fitness) 
        
        if plot_results:
            plt.plot(np.ones_like(avg_arr) * max_fitness, label='limit', linestyle='--')
            plt.plot(avg_arr/num_run, label='avg')
            plt.plot(min_arr/num_run, label='min')
            plt.plot(max_arr/num_run, label='max')
            plt.legend(loc='lower right')
            plt.title(s="pX = " + str(self.crossover_prob) + ", pM = " + str(self.mutation_prob))
            plt.ylim((0,max_fitness * 1.1))
            plt.show()
        return avg_arr, min_arr, max_arr, max_fitness

    def run_ga_optimization(
            self,
            num_generation,
        ):
        avg_arr = np.zeros(shape=(num_generation,))
        min_arr = np.zeros(shape=(num_generation,))
        max_arr = np.zeros(shape=(num_generation,))

        for i in range(0, num_generation):
            # evaluate fitness for current population
            fitnesses, max_fitness = self.function.evaluate_fitness(self.population)

            # run the GA steps
            # fitness proportional selection
            self.population.fitness_proportional_selection(fitnesses)
            # mutation 
            self.population.mutate()
            # crossover
            self.population.single_crossover()

            # log the statistics 
            avg_arr[i], min_arr[i], max_arr[i] = self.calc_fitness_stats(fitnesses)
        return avg_arr, min_arr, max_arr, max_fitness

    def calc_fitness_stats(
            self, 
            fitnesses
        ):
        # TODO: calculate min, max, average fitness for current population state
        max_fit = np.max(fitnesses)
        min_fit = np.min(fitnesses)
        avg_fit = np.average(fitnesses)
        return avg_fit, min_fit, max_fit












