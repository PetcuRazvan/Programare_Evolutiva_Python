import numpy as np
import matplotlib.pyplot as plt
import copy
import random

def OCX(x, y):
    n = x.size
    pozitii = np.random.choice(n, 2, False)
    i = min(pozitii)
    j = max(pozitii)
    start_poz = j
    lungime_copiata = j - i + 1

    print(lungime_copiata)
    print(x)
    print(y)
    print(f'Crossover intre pozitiile {i} si {j}')

    c1 = [None] * n
    c2 = [None] * n

    c1[i : j + 1] = x[i : j + 1]
    c2[i : j + 1] = y[i : j + 1]

    poz_sursa = start_poz
    poz_destinatie = start_poz + 1
    lungime_de_copiata = n - lungime_copiata
    while lungime_de_copiata > 0:
        if poz_sursa == n:
            poz_sursa = 0

        if poz_destinatie == n:
            poz_destinatie = 0

        if y[poz_sursa] in c1:
            poz_sursa += 1
            continue

        c1[poz_destinatie] = y[poz_sursa]
        poz_sursa += 1
        poz_destinatie += 1
        lungime_de_copiata -= 1

    poz_sursa = start_poz
    poz_destinatie = start_poz + 1
    lungime_de_copiata = n - lungime_copiata
    while lungime_de_copiata > 0:
        #print('whileul asta se face la infinit?')

        if poz_sursa == n:
            poz_sursa = 0

        if poz_destinatie == n:
            poz_destinatie = 0

        if x[poz_sursa] in c2:
            poz_sursa += 1
            continue

        c2[poz_destinatie] = x[poz_sursa]
        poz_sursa += 1
        poz_destinatie += 1
        lungime_de_copiata -= 1

    c1 = np.array(c1) #convertire inapoi la np.array
    c2 = np.array(c2)

    return c1, c2

if __name__ == '__main__':
    n = 8
    x = np.random.permutation(n)
    y = np.random.permutation(n)

    c1, c2 = OCX(x, y)
    print(c1)
    print(c2)