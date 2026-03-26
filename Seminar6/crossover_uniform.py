import numpy as np
import matplotlib.pyplot as plt
import copy
import random

def obiectiv(x, v, c, cmax):
    cost = np.dot(x, c)
    valoare = np.dot(x, v)

    valid = cost <= cmax

    return valid, valoare

def generare_populatie(v, c, cmax, dim):
    n = v.size
    populatie = np.zeros(shape = [dim, n + 1], dtype = int)

    for i in range(dim):
        valid = False

        while not valid:
            x = random.choices([0, 1], k = n)
            valid, valoare = obiectiv(x, v, c, cmax)

        x.append(valoare)
        populatie[i] = x

    return populatie

def crossover_uniform(x, y):
    """
    Crossover uniform
    :param x: Primul parinte
    :param y: Al doilea parinte
    :return: Cei 2 descendenti
    """

    c1 = copy.deepcopy(x)
    c2 = copy.deepcopy(y)

    n = len(x)

    for i in range(n):
        p = np.random.randint(2) > 0.5 #ca sa ne dea bool
        if p:
            c1[i] = y[i]
            c2[i] = x[i]
        else:
            c1[i] = x[i]
            c2[i] = y[i]

    return c1, c2


def crossover_populatie(populatie, pc, c, v, cmax):
    dim = len(populatie)
    n = populatie.shape[1] - 1

    new_generation = copy.deepcopy(populatie)

    for i in range(0, dim, 2):
        x = populatie[i]
        y = populatie[i + 1]

        r = np.random.uniform(0, 1)
        if r <= pc:
            c1, c2 = crossover_uniform(x, y)
            valid, valoare = obiectiv(c1[:-1], v, c, cmax)
            if valid:
                c1[len(c1) - 1] = valoare
                new_generation[i] = c1

            valid, valoare = obiectiv(c2[:-1], v, c, cmax)
            if valid:
                c2[len(c2) - 1] = valoare
                new_generation[i + 1] = c2

    return new_generation

if __name__ == '__main__':
    c = np.genfromtxt('cost.txt')
    v = np.genfromtxt('valoare.txt')
    pc = 0.8

    cmax = 50
    dim = 10
    populatie = generare_populatie(v, c, cmax, dim)
    new_gen = crossover_populatie(populatie, pc, c, v, cmax)

    plt.plot([populatie[i, -1] for i in range(dim)], 'bs', markersize = 11)
    plt.plot([new_gen[i, -1] for i in range(dim)], 'rs', markersize = 6)
    plt.xlabel('Populatie')
    plt.ylabel('Fitness')

    plt.show()