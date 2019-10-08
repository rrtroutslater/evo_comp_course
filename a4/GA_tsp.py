from population_tsp import * 
from util import *
import matplotlib.pyplot as plt

# genetic alg
# 

class gaTSP():
    def __init__(self,
            population,
            crossover_prob=0.7,
            mutation_prob=0.0004,
            ):
        
        self.p = population
        self.crossover_prob = crossover_prob
        self.mutation_prob = mutation_prob

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

        best_idx = 0
        best_fit = 0
        best_individual = np.zeros_like(self.p.p_idx[0])
        for i in range(0, num_run):
            self.p = PopulationTSP(self.p.p_idx.shape[0], self.p.tsp_dict)
            x, y, z, max_fitness, best_fit_new, best_individual_new = self.run_ga_optimization(num_generation)
            # print('\nBEST AFTER FUNCTION RETURN\n', best_individual_new)
            if best_fit_new > best_fit:
                best_fit = best_fit_new 
                best_individual = best_individual_new
            avg_arr += x 
            min_arr += y 
            max_arr += z

        # if verbose:
            # print('example best population member:\n', \
            #     np.reshape(best_individual, self.function.pop_shape), 
            # )
            # print('in decimal:\n', bin_arr_to_dec_arr(
            #     np.expand_dims(np.reshape(best_individual, self.function.pop_shape), axis=0), 
            #     self.function.bounds)
            #     )
            # print('corresponding fitness:\t\t\t', best_fit)
            # print('avg max fitness at end:\t\t\t', max_arr[z.shape[0]-1]/num_run)
            # print('avg fitness at end:\t\t\t', avg_arr[x.shape[0]-1]/num_run)
            # print('max possible fitness (theoretical):\t', max_fitness) 

        if plot_results:
            plt.plot(np.ones_like(avg_arr) * max_fitness, label='limit', linestyle='--')
            plt.plot(avg_arr/num_run, label='avg')
            plt.plot(min_arr/num_run, label='min')
            plt.plot(max_arr/num_run, label='max')
            plt.legend(loc='lower right')
            plt.title(s="pX = " + str(self.crossover_prob) + ", pM = " + str(self.mutation_prob))
            plt.ylim((min([0,np.min(min_arr)]),max_fitness * 1.1))
            plt.show()
        return avg_arr, min_arr, max_arr, max_fitness

    def run_ga_optimization(self,
            num_generation
            ):
        avg_arr = np.zeros(shape=(num_generation,))
        min_arr = np.zeros(shape=(num_generation,))
        max_arr = np.zeros(shape=(num_generation,))

        best_fit = 0
        best_individual = np.zeros_like(self.p.p_idx[0])

        max_fitness = self.p.max_distance

        for i in range(0, num_generation):
            # evaluate fitness for current population
            
            fitness = self.p.calc_pop_fitness()
            avg_arr[i], min_arr[i], max_arr[i] = self.calc_fitness_stats(fitness)

            if np.max(fitness) > best_fit:
                best_fit = np.max(fitness)
                best_individual[:] = self.p.p_idx[np.argmax(fitness)][:]

            self.p.elite_selection(fitness)

            self.p.crossover_pmx(crossover_prob=self.crossover_prob)

            self.p.swap_mutation(mutation_prob=self.mutation_prob)

        return avg_arr, min_arr, max_arr, max_fitness, best_fit, best_individual

    def calc_fitness_stats(
            self, 
            fitnesses
        ):
        max_fit = np.max(fitnesses)
        min_fit = np.min(fitnesses)
        avg_fit = np.average(fitnesses)
        return avg_fit, min_fit, max_fit