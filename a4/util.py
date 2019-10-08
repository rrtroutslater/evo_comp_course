import os 
import numpy as np 


def parse_tsp(fname):

    f = open(fname, 'r')
    # r = f.read()
    int_str_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    tsp_dict = {}
    for line in f:
        print(line)
        l = line.split()
        print(l)
        if l[0] in int_str_list:
            tsp_dict[l[0]] = np.array([float(l[1]), float(l[2])])
    return tsp_dict



