import numpy as np


def main():
    num_gen = np.array([
        50, 139, 973, 257, 269, 
        428, 183, 146, 1141, 451, 
        1261, 206, 101, 99, 808, 
        530, 604, 517, 169, 457
    ])

    print('number of runs:', num_gen.shape[0])
    print('average:\t', np.mean(num_gen))
    print('stdev:\t\t', np.std(num_gen))
    print('min:\t\t', np.min(num_gen))
    print('max:\t\t', np.max(num_gen))


if __name__ == "__main__":
    main()
