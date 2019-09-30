import numpy as np 
import random

class Population(object):
    def __init__(self,
            pop_size,
            bits,
            mutation_prob=0.001,
            crossover_prob=0.7,
            ):

        self.pop_size = pop_size
        self.bits = bits 
        self.mutation_prob = mutation_prob
        self.crossover_prob = crossover_prob
        
        self.p = np.random.choice([0,1], size=(self.pop_size, self.bits))
        self.threshold = np.ones_like(self.p) * self.mutation_prob
        print('created a population with shape:\t', self.p.shape)
        return

    def fitness_proportional_selection(self,
            fitness,
            ):
        """ 
        assumes fitness[i] is fitness for the ith member of the population

        applies fitness proportional selection to population contained in class instance
        """
        prob_dist = fitness / np.sum(fitness)
        idx = np.random.choice(np.array(range(prob_dist.shape[0])), size=self.p.shape[0], p=prob_dist)
        # print(idx)
        # print('idx shape:', idx.shape)
        # print(self.p.shape)
        self.p[:] = self.p[idx]
        # print(self.p)
        # self.p = np.random.choice(self.p, size=self.p.shape, p=prob_dist)
        return

    def single_crossover(self,):
        """
        """
        new_pop = np.zeros_like(self.p)
        idx = 0
        for individual in self.p:
            if random.random() < self.crossover_prob:
                partner_idx = np.random.choice(range(self.p.shape[0]))
                partner = self.p[partner_idx]
                # partner = np.random.choice(self.p)
                crossover_idx = np.random.randint(0, self.bits)
                new_pop[idx][:crossover_idx] = individual[:crossover_idx]
                new_pop[idx][crossover_idx:] = partner[crossover_idx:]
            else:
                new_pop[idx] = individual
            idx += 1
        self.p = new_pop
        return

    def mutate(self,):
        """
        """
        flip_idx = np.argwhere(np.random.random(size=self.p.shape) < self.threshold)
        for i in flip_idx:
            self.p[i[0]][i[1]] -= 1
        zero_idx = np.argwhere(self.p < 0)
        for i in zero_idx:
            self.p[i[0]][i[1]] += 1
        return
