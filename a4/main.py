from __future__ import print_function
from population_tsp import *
from util import *


def main():
    data_dir = './tsps/data/'
    pop_size = 40

    for fn in os.listdir(data_dir):
        tsp_dict = parse_tsp(data_dir + fn)
        p = PopulationTSP(pop_size, tsp_dict)
        # print(p.p_idx)
        f = p.calc_pop_fitness()
        # print(f)
        p.elite_selection(f)
        p.crossover_pmx()
        # print(p.p_idx)

        p.swap_mutation()
        return

    return


if __name__ == "__main__":
    main()