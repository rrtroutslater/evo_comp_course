from __future__ import print_function
import numpy as np 
from dejong_functions import *
from util import *


# genetic algorithm class
"""
fitness proportional selection

uniform crossover

random bitwise mutation

must pass a fitness function to eval?

assume that bit strings have length 150

-> binary to decimal function will need to know the appropriate bounds

-> 
"""

def main():
    # dejong 1
    n_bits = 15
    x = np.zeros(shape=(10, 3, n_bits))
    dejong_1(x)

    return


if __name__ == "__main__":
    main()
    pass