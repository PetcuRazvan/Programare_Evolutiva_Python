import numpy as np
import matplotlib.pyplot as grafic

def fobNR(x):
    """
    functia calculeaza numaryl de perechi de regine care nu se ataca
    :param x: list
    :return: int
    """
    n = x.size
    c = n * (n - 1) / 2
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(i - j) == abs(x[i] - x[j]):
                c -= 1
    return c

def gen(n, dim):
    population = np.zeros((dim, n + 1), dtype = int)
    for i in range(dim):
        population[i, :n] = np.random.permutation(n)
        population[i][n] = fobNR(population[i, :n])  #pot sa folosesc population[i, n] inloc de population[i][n]

    return population

def deseneaza(population, n, dim):
    x = [i for i in range(dim)]
    y = [population[i][n] for i in range(dim)]
    grafic.plot(x, y, "gs", markersize = 10)
    grafic.show()

if __name__ == "__main__":
    p = gen(8, 30)
    print(p)
    deseneaza(p, 8, 30)