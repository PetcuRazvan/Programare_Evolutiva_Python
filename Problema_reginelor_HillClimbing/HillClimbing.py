import numpy as np

def get_solutie_aleatoare(n):
    """
    Functia genereaza o solutie aleatoare pentru o tabla de nxn
    :param n: dimensiunea tablei
    :return: o lista cu solutii aleatoare
    """
    pozitii = [i for i in range(1, n + 1)]

    solutie = []
    while len(pozitii) != 0:
        locatie = pozitii[np.random.randint(0, len(pozitii))]
        solutie.append(locatie)

        pozitii.remove(locatie)

    return solutie

def get_vecini(solutie):
    """
    Functia genereaza toti vecinii unei solutii
    :param solutie: o lista, reprrezentand o solutie
    :return: o lista de liste, reprezentand vecinii solutiei
    """
    vecini = []
    for i in range(len(solutie)):
        for j in range(i + 1, len(solutie)):
            vecin = [i for i in solutie]

            vecin[i] = solutie[j]
            vecin[j] = solutie[i]


            vecini.append(vecin)

    return vecini

def functia_obiectiv(solutie):
    """
    Functia calculeaza numarul de perechi de regine care se ataca
    :param solutie: o lista, reprrezentand o solutie
    :return: numarul de perechi de regine care se ataca
    """
    numar_perechi = 0

    for i in range(len(solutie) - 1):
        for j in range(i + 1, len(solutie)):
            distanta_x_patrat = (solutie[j] - solutie[i]) ** 2
            distanta_y_patrata = (j - i) ** 2

            if distanta_x_patrat == distanta_y_patrata:
                numar_perechi += 1

    return numar_perechi

def hill_climbing(numar_solutii_initiale, n):
    """
    Efectueaza Hill climbing pentru a determina minimul functie oniectiv
    :param numar_solutii_initiale: numarul de solutii alese aleator initial
    :param n: dimensiunea tablei
    :return: o lista, reprezentand cea mai buna solutie gasita
    """
    X = [None] * numar_solutii_initiale
    Y = [None] * numar_solutii_initiale

    for i in range(numar_solutii_initiale):
        solutie_curenta = get_solutie_aleatoare(n)

        local = False
        while not local:
            valoare_curenta = functia_obiectiv(solutie_curenta)
            vecini = get_vecini(solutie_curenta)
            valori_vecini = [functia_obiectiv(i) for i in vecini]

            valoare_min = min(valori_vecini)
            poz = valori_vecini.index(valoare_min)
            vecin_min = vecini[poz]

            if valoare_min < valoare_curenta:
                solutie_curenta = vecin_min
            else:
                local = True

        X[i] = solutie_curenta
        Y[i] = functia_obiectiv(solutie_curenta)

    min_global = min(Y)
    poz = Y.index(min_global)

    return X[poz]

def afiseaza_solutie(solutie):
    for i in range(len(solutie)):
        for j in range(len(solutie)):
            if j == solutie[i] - 1:
                print('Q  ', end = "")
            else:
                print('.  ', end = "")
        print()
    print()

if __name__ == '__main__':
    solutie = hill_climbing(10, 8)

    afiseaza_solutie(solutie)
    print(f'Perechi de regine care se ataca: {functia_obiectiv(solutie)}')
