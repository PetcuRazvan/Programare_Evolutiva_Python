import numpy as np
import matplotlib.pyplot as grafic
from math import sin, cos

def functie_obiectiv(x):
    return x ** 3 * sin(x / 3) + x ** 3 * cos(2 * x) - x * sin(3 * x) + x * cos(x)

def get_vecini(x, nr, pas, a, b):  #apesi de 3 ori pe " si enter si iti genereaza sablon pentru documentatie ... cool
    """
    Functie care genereaza vectorul de vecini si valorile corezpunzatoare
    :param x: punctul initial
    :param nr: numarul de vecini in fiecare directie = 2nr
    :param pas: distanta dintre vecini
    :param a: limita de jos a intervalului de definire a functiei
    :param b: limita de sus a intervalului de definire a functiei
    :return: vectorul de vecini si vectorul de valori corespunzatoare ale functiei in aceasta ordine
    """
    vecini = []
    valori = []

    for i in range(-nr, nr + 1):
        vecin = x + i * pas
        if vecin >= a and vecin <= b:
            vecini.append(vecin)
            valori.append(functie_obiectiv(vecin))

    return vecini, valori

def HC(a, b, nrp, nrv, pas):
    """
    Efectueaza HillClimbing pentru a nimeri maximul functiei
    :param a: limita de jos a intervalului
    :param b: limita de sus a intervalului
    :param nrp: numarul de puncte initiale
    :param nrv: numarul de vecini pe fiecare directie pemntru fiecare punct
    :param pas: distanta dintre vecini
    :return: punctul de maxim si valoarea maxima a functiei in aceasta ordine
    """
    X = [None] * nrp
    Y = [None] * nrp

    for i in range(nrp):
        pc = np.random.uniform(a, b)

        local = False
        while not local:
            vc = functie_obiectiv(pc)
            vecini, valori = get_vecini(pc, nrv, pas, a, b)

            valmax = max(valori)
            poz = valori.index(valmax)  #am luat indexul valorii maxime ca sa luam vecinul din vectorul de vecini
            vecmax = vecini[poz]
            if valmax > vc:
                pc = vecmax
            else:
                local = True

        X[i] = pc
        Y[i] = vc #what!!! lui Python nu ii pasa daca vc e out of scope ... cool

    maxglobal = max(Y)
    poz = Y.index(maxglobal)
    punctmaxglobal = X[poz]

    desenare(a, b, punctmaxglobal, maxglobal, X, Y)

    return punctmaxglobal, maxglobal

def desenare(a, b, xmax, ymax, X, Y):
    x = np.arange(a, b, 0.01)
    y = [functie_obiectiv(i) for i in x]

    grafic.plot(x, y, 'k-') #k de la black(b de la blue, r de la red) iar - vine de la linie continua(. ne face linie punctata, -- ne face linie intrerupta)
    grafic.plot(X, Y, 'b.', label = 'optim local')
    grafic.plot(xmax, ymax, 'r*', label = 'optim global calculat')
    grafic.title('Graficul functiei f')
    grafic.legend()
    grafic.show()

if __name__ == "__main__":
    pm, vm = HC(0, 50, 100, 100, 0.01)
    print(f"Maximul global gasit al functiei este {pm} in punctul {vm}")

    #facem grafic fortaaaaa
