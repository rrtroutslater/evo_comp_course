from __future__ import print_function
from population_tsp import *
from GA_tsp import *
from util import *


def main():
    data_dir = './tsps/data/'
    pop_size = 50

    for fn in os.listdir(data_dir):
        tsp_dict = parse_tsp(data_dir + fn)
        p = PopulationTSP(pop_size, tsp_dict)
        ga = gaTSP(p)
        ga.run_ga(fn, num_generation=100, num_run=30)

        # return

    return


if __name__ == "__main__":
    main()