import numpy as np



def plot_results():
    """
    """
    return

# def dec_to_bin(x, n_bits):
#     """
#     x : (N,) numpy array of ints in base 10
#     n_bits : number of bits of binary representation (must be sufficient)
#     """
#     for n in x:
#         assert n < 2**n_bits
#     nums = np.zeros(shape=(x.shape[0], n_bits))
#     for i in range(0, n_bits):
#         nums[:,i] = (x[:]/(2**(n_bits - i - 1))).astype(np.int)
#         x[:] -= (2**(n_bits - i - 1)) * ((x[:]/(2**(n_bits - i - 1))).astype(int) > 0).astype(np.int)
#     return nums

# def decode(x, n_min, n_max):
#     """
#     decodes a binary number 
#     """
#     n = np.ceil(np.log2(n_max - n_min))
#     p = (n_max - n_min) / (2**n)
#     return n_min + bin_to_dec(x) * p

