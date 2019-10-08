import numpy as np 



class PopulationTSP():
    def __init__(self,
            num_city,
            pop_size,
            ):
        
        self.pop_size = pop_size 
        self.num_city = num_city
        self.pop = self.generate_pop()

    def generate_pop(self,):
        p = np.zeros(shape=(self.pop_size, self.num_city))
        int_arr = np.arange(0, self.num_city, 1)
        for i in range(0, p.shape[0]):
            p[i] = np.random.choice(int_arr, size=p.shape[1], replace=False)
        return p

    def crossover_pmx(self, 
            ):
        #TODO
        return
    
    def mutate_pmx(self,
            ):
        # TODO
        return 
