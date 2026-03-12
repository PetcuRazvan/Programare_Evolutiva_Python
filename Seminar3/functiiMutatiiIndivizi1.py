import numpy as np
import random
import copy

def m_perm_amestecare(x):
    """
    Mutatie prin amestecare a permutarii x
    :param x: permutarea careia se aplica mutatia
    :return: amestecarea obtinuta dupa aplicarea mutatiei
    """
    n = len(x)
    indexi = [x for x in range(n)]

    poz = [None] * 2
    poz[0] = random.choice(indexi)
    indexi.remove(poz[0])
    poz[1] = random.choice(indexi)

    i = min(poz)
    j = max(poz)
    print(i, j)

    mutatie = x.copy()
    sector = mutatie[i : j + 1]
    for k in range(i, j + 1):
        mutatie[k] = random.choice(sector)
        sector.remove(mutatie[k])

    return mutatie

def m_prin_interschimbare(x):
    n = len(x)
    indexi = [x for x in range(n)]

    i = random.choice(indexi)
    indexi.remove(i)
    j = random.choice(indexi)
    print(i, j)

    mutatie = x.copy()
    mutatie[i] = x[j]
    mutatie[j] = x[i]

    return mutatie

if __name__ == "__main__":
    mutatie = m_perm_amestecare([1,2,3,4,5,6,7,8])
    print(mutatie)

    mutatie = m_prin_interschimbare([1,2,3,4,5,6,7,8])
    print(mutatie)