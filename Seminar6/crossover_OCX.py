import numpy as np
import matplotlib.pyplot as plt
import copy
import random

def OCX(x, y):
    n = x.size
    pozitii = np.random.choice(n, 2, False)
    i = min(pozitii)
    j = max(pozitii)
    print(x)
    print(y)
    print(f'Crossover intre pozitiile {i} si {j}')

    c1 = copy.deepcopy(x)
    c2 = copy.deepcopy(y)

    #de facut acasa

    return c1, c2

if __name__ == '__main__':
    n = 8
    x = np.random.permutation(n)
    y = np.random.permutation(n)

    c1, c2 = OCX(x, y)
    print(c1)
    print(c2)