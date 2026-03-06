import random
import numpy as np
import matplotlib.pyplot as grafic

def obiectiv(x, c, v, max):
    """
    Functie ce calculeaza valoarea obiectelor din ghiozdan si specifica daca este depasit costul maxim
    :param x: vectorul ce reprezinta individul
    :param c: vectorul de costuri
    :param v: vectorul de valori
    :param max:
    :return: O valoare de tip boolean
            Valoarea obiectelor din ghiozdan daca individul este fezabil
    """
    val = np.dot(x, v)
    cost = np.dot(x, c)

    return cost <= max

def gen(fc, fv, max, dim):
    c = np.genfromtxt(fc)
    v = np.genfromtxt(fv)

    n = v.size
    pop = []
    for i in range(dim):
        x = [random.choice([0, 1]) for _ in range(n)]
        while not obiectiv(x, c, v, max):
            x = [random.choice([0, 1]) for _ in range(n)] #iterez pana cand x este o solutie fezabila

        x.append(obiectiv(x, c, v, max))
        pop.append(x)

    return pop

def reprezinta(pop, dim, n):
    x = [i for i in range(dim)]
    y = [pop[i][n] for i in range(dim)]

    grafic.plot(x, y, "gs", markersize=10)
    grafic.show()

if __name__ == "__main__":
    p = gen("cost.txt", "valoare.txt", 50, 10)
    for element in p:
        print("Individ: ", element[:-1])
        print("     calitate: ", element[-1])

    reprezinta(p, 10, len(p[0]) - 1)