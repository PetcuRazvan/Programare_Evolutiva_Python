import numpy as np
import matplotlib.pyplot as plt
from math import sin

def fitness(x):
    return 1 + sin(2 * x[0] - x[2]) + ((x[1] * x[3]) ** (1/3))

def generare_populatie(dim, a, b):
    populatie = []

    for _ in range(dim):
        individ = []
        for i in range(len(a)):
            individ.append(np.random.uniform(a[i], b[i]))

        individ.append(fitness(individ))

        populatie.append(individ)

    return populatie

def mutatie(x, a, b, sigma):
    e = np.random.normal(0, sigma)

    y = x + e
    if y < a:
        y = a

    if y > b:
        y = b

    return y

def mutatie_populatie(populatie, a, b, sigma, p):
    m_populatie = np.copy(populatie)
    n = len(populatie)

    for i in range(n):
        mutat = False

        for j in range(4):
            if np.random.uniform(0, 1) < p:
                m_populatie[i][j] = mutatie(m_populatie[i][j], a[j], b[j], sigma)
                mutat = True

        if mutat:
            m_populatie[i][-1] = fitness(m_populatie[i][:-1])

    return m_populatie

if __name__ == "__main__":
    a = [-1, 0, 0, 0]
    b = [1, 0.2, 1, 5]
    dim = 15
    sigma = 0.2

    populatie = generare_populatie(dim, a, b)

    m_pop = mutatie_populatie(populatie, a, b, sigma, 0.2)

    plt.plot([populatie[i][-1] for i in range(dim)], 'bs', ms = 8, label = 'populatie')
    plt.plot([m_pop[i][-1] for i in range(dim)], 'gs', ms = 5, label = 'populatie mutata')
    plt.ylabel('Fitness')
    plt.legend()
    plt.show()