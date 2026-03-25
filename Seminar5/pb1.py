import random

import numpy as np
import matplotlib.pyplot as plt

def fitness(x):
    n = len(x)
    nr = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if x[i] < x[j]:
                nr += 1
    return nr

def generare_populatie(n,dim):
    populatie = np.zeros([dim, n+1], dtype=int)

    for i in range(dim):
        permutare = np.random.permutation(n)
        populatie[i][:-1] = permutare
        populatie[i][-1] = fitness(permutare)

    return populatie

def mutatie_interschimbare(x):
    copie = np.copy(x)
    n = len(x)
    poz = [i for i in range(n)]
    i = random.choice(poz)
    poz.remove(i)
    j = random.choice(poz)
    copie[i], copie[j] = copie[j], copie[i]

    return copie

def mutatie_amestec(x):
    copie = np.copy(x)
    n = len(x)

    poz = [i for i in range(n)]
    i = random.choice(poz)
    poz.remove(i)
    j = random.choice(poz)

    i, j = min(i, j), max(i, j)
    print(i, j)

    poz = [k for k in range(i, j + 1)]
    for k in range(i, j + 1):
        index = random.choice(poz)
        poz.remove(index)

        copie[k] = x[index]

    return copie

def mutatie_populatie(populatie, p):
    dim = populatie.shape[0]

    copie=np.copy(populatie)
    for i in range(dim):
        pb = np.random.uniform(0,1)
        if pb <= p:
            copie[i][:-1] = mutatie_interschimbare(copie[i][:-1])
            copie[i][-1] = fitness(copie[i][:-1])
    return copie

if __name__ == "__main__":
    n = 8
    dim = 10
    p = 0.2
    populatie = generare_populatie(n,dim)
    #print(populatie)

    populatie_mutata = mutatie_populatie(populatie,p)

    plt.plot([populatie[i][-1] for i in range(dim)], 'bs', ms = 8, label = 'Populatie initiala')
    plt.plot([populatie_mutata[i][-1] for i in range(dim)], 'rs', ms = 5, label = 'Populatie mutata')

    plt.legend()
    plt.ylabel('Fitness')
    plt.show()