import numpy as np 

# population class

class Population(object):
    def __init__(self,
            pop_size,
            bits,
            mutation_prob=0.001,
            crossover_prob=0.7,
            ):

        self.pop_size = pop_size
        self.bits = bits 
        self.p = np.random.choice([0,1], size=(self.pop_size, self.bits))

    def fitness_proportional_selection(self,
            fitness,
            ):
        """ 
        assumes fitness[i] is fitness for the ith member of the population

        applies fitness proportional selection to population contained in class instance
        """
        prob_dist = fitness / np.sum(fitness)
        self.p = np.random.choice(self.p, size=self.p.shape, p=prob_dist)

    def crossover(self,
            ):
        

        return

    def mutate(self,):

        for i in range(0, self.p.shape[0]):
            for j in range(0, self.p.shape[1]):




        return