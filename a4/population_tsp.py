from __future__ import print_function
import numpy as np 

class PopulationTSP():
    def __init__(self,
            pop_size,
            tsp_dict,
            elite_pct=0.10,
            ):

        self.pop_size = pop_size
        self.tsp_dict = tsp_dict
        self.elite_pct = elite_pct
        self.num_city = len(tsp_dict.keys())
        self.p_idx = self.generate_pop()
        self.max_distance = self.calc_max_distance()
        print('')
        print(self.p_idx.shape)
        return

    def calc_max_distance(self,):
        """ 
        max fitness for n_c cities is (n_c-1) max_intracity_distance
        """
        max_dist = 0
        for i in range(self.p_idx.shape[1]):
            for j in range(self.p_idx.shape[1]):
                dist = np.sqrt(
                    (self.tsp_dict[i+1][0] - self.tsp_dict[j+1][0])**2 \
                    + (self.tsp_dict[i+1][1] - self.tsp_dict[j+1][1])**2 \
                )
                if dist > max_dist:
                    max_dist = dist

        max_dist_total = (self.p_idx.shape[1] - 1) * max_dist
        return max_dist_total.astype(int)

    def generate_pop(self,):
        p_idx = np.zeros(shape=(self.pop_size, self.num_city))
        int_arr = np.arange(1, self.num_city+1, 1)
        for i in range(0, p_idx.shape[0]):
            p_idx[i] = np.random.choice(int_arr, size=p_idx.shape[1], replace=False)
        return p_idx

    def calc_pop_fitness(self,):
        # fitness = minimizing euclidean distance
        d_total = np.zeros(shape=(self.p_idx.shape[0],))

        for i in range(0, self.p_idx.shape[0]):
            for j in range(0, self.p_idx.shape[1] - 1):
                d_total[i] += np.sqrt(
                    (self.tsp_dict[self.p_idx[i][j]][0] - self.tsp_dict[self.p_idx[i][j+1]][0])**2 \
                    + (self.tsp_dict[self.p_idx[i][j]][1] - self.tsp_dict[self.p_idx[i][j+1]][1])**2 \
                ).astype(int)

        fitness = self.max_distance - d_total
        return fitness

    def elite_selection(
            self,
            fitness,
            ):
        """
        """
        num_best = int(self.pop_size * self.elite_pct)

        # set num_best first indices in self.p_idx to be num_best fittest individuals
        best_idx = np.argpartition(-fitness, num_best)[:num_best]
        print('\nbest fitness:', fitness[best_idx])
        next_p_idx = np.zeros_like(self.p_idx)
        for i in range(0, num_best):
            next_p_idx[i] = self.p_idx[best_idx[i]]

        idx = num_best
        for i in range(0, self.p_idx.shape[0]):
            if i not in best_idx:
                next_p_idx[idx] = self.p_idx[i]
                idx += 1

        self.p_idx = next_p_idx
        return

    def crossover_pmx(self, 
            crossover_prob = 0.7,
            ):
        """
        """
        num_best = int(self.pop_size * self.elite_pct)

        # assumes first few indices correspond to most fit, these will remain unaltered
        next_p_idx = np.zeros_like(self.p_idx)
        for i in range(0, num_best):
            next_p_idx[i] = self.p_idx[i]

        # pmx crossover for remainder of population
        for i in range(num_best, self.p_idx.shape[0]):
            # randomly select two parents
            idx = np.random.randint(0, self.p_idx.shape[0])
            p1 = self.p_idx[idx]
            idx = np.random.randint(0, self.p_idx.shape[0])
            p2 = self.p_idx[idx]

            # initialize child arrays
            c2 = np.zeros_like(p1)

            # length of interval to pass down to child
            interval_len = np.random.randint(0, self.p_idx.shape[1])
            if np.random.rand() < crossover_prob:
                # starting index of interval to copy
                start_idx = np.random.randint(0, self.p_idx.shape[1] - interval_len)

                for j in range(0, self.p_idx.shape[1]):
                    if j >= start_idx and j < start_idx + interval_len:
                        # get array values from first parent
                        c2[j] = p1[j]
                    elif p2[j] not in p1[start_idx : interval_len].tolist() \
                            and p2[j] not in p2[start_idx : interval_len].tolist():
                        c2[j] = p2[j]
                    elif p2[j] not in p2[start_idx : interval_len].tolist() \
                            and p2[j] in p1[start_idx : interval_len].tolist():
                        x = p2[j] 
                        c2[j] = p2[np.argwhere(p1 == x)]
                    else:
                        print('unhandled case in PMX crossover')
                
                next_p_idx[i] = c2
            else:
                next_p_idx[i] = self.p_idx[i]

        self.p_idx = next_p_idx
        return

    def swap_mutation(self,
            mutation_prob = 0.004
            ):
        for i in range(0, self.p_idx.shape[0]):
            if np.random.rand() < mutation_prob:
                idx_1 = np.random.randint(0, self.p_idx.shape[1])
                idx_2 = np.random.randint(0, self.p_idx.shape[1])

                tmp = self.p_idx[i][idx_1]
                self.p_idx[i][idx_1] = self.p_idx[i][idx_2]
                self.p_idx[i][idx_2] = tmp
        return         







