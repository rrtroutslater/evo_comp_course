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

    def calc_distance(self, individual):
        x = individual
        d_total = 0 
        for i in range(0, x.shape[0] - 1):
            d_total += np.sqrt((self.tsp_dict[x[i]][0] - self.tsp_dict[x[i+1]][0])**2 \
                + (self.tsp_dict[x[i]][1] - self.tsp_dict[x[i+1]][1])**2
            )
        return d_total

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
        num_best = int(self.pop_size * self.elite_pct)

        # set num_best first indices in self.p_idx to be num_best fittest individuals
        best_idx = np.argpartition(-fitness, num_best)[:num_best]
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

    def get_child_idx(self, elem, p1, p2, c1, start_idx, end_idx):
        # index of a value in parent 2, also in the child
        idx_p2 = np.where(p2 == elem)[0]

        # parent 1 value at index above
        val1 = p1[idx_p2]

        # parent 2 value 
        idx_p2_0 = np.where(p2 == val1)[0]

        if 0:
            print('------------')
            print('idx_p2:\t\t', idx_p2)
            print('val1:\t\t', val1)
            print('idx_p2_0:\t', idx_p2_0)
            print('c1 in gci\n',c1)
            x = input()

        if idx_p2_0 < start_idx or idx_p2_0 >=  end_idx:
                # and p2[idx_p2_0] not in c1:
            return idx_p2_0
        else:
            return self.get_child_idx(p2[idx_p2_0], p1, p2, c1, start_idx, end_idx)

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
            if np.random.rand() < crossover_prob:
                # randomly select two parents
                idx = np.random.randint(0, self.p_idx.shape[0])
                p1 = self.p_idx[idx]
                idx = np.random.randint(0, self.p_idx.shape[0])
                p2 = self.p_idx[idx]

                # initialize child arrays
                c1 = np.ones_like(p1) * -1

                # length of interval to pass down to child
                interval_len = np.random.randint(1, self.p_idx.shape[1]-1)
                # starting index of interval to copy
                start_idx = np.random.randint(0, self.p_idx.shape[1] - interval_len)


                c1[start_idx:start_idx+interval_len] = p1[start_idx:start_idx+interval_len]

                if 0:
                    print('-----------------------------------')
                    print('interval:\t', interval_len)
                    print('start idx:\t', start_idx)
                    print(p1)
                    print(p2)
                    print(c1)
                    print('-----------------------------------')

                for j in range(start_idx,  start_idx + interval_len):
                    if p2[j] not in c1.tolist():
                        # if p2[j] not in c1[start_idx:start_idx+interval_len].tolist():
                        idx = self.get_child_idx(
                            p2[j], p1, p2, c1, start_idx, start_idx+interval_len
                        )
                        c1[idx] = p2[j]
                
                for j in range(0, p2.shape[0]):
                    if c1[j] == -1:
                        c1[j] = p2[j]

                next_p_idx[i] = c1
                # print('\nafter crossover:\n', c1)
                if np.unique(c1).shape[0] != p1.shape[0]:
                    print('DUPLICATES IN A CHILD')
                    return
            else:
                next_p_idx[i] = self.p_idx[i]

        self.p_idx = next_p_idx
        return

    def swap_mutation(self,
            mutation_prob = 0.004
            ):
        num_best = int(self.pop_size * self.elite_pct)
        for i in range(num_best, self.p_idx.shape[0]):
            if np.random.rand() < mutation_prob:
                idx_1 = np.random.randint(0, self.p_idx.shape[1])
                idx_2 = np.random.randint(0, self.p_idx.shape[1])
                tmp = self.p_idx[i][idx_1]
                self.p_idx[i][idx_1] = self.p_idx[i][idx_2]
                self.p_idx[i][idx_2] = tmp
        return         


