from population_tsp import *
from util import *



def main():
    p = PopulationTSP(10, 5)
    print(p.pop)

    tsp_dict = parse_tsp('./tsps/data/burma14.tsp')
    print(tsp_dict)

    return

if __name__ == "__main__":
    main()