from operator import truediv

import matplotlib.pyplot as plt

def nrLiniiCrescatoare(matrice):
    nr = 0
    for linie in matrice:
        crescator = True
        for i in range(len(linie) - 1):
            if linie[i] >= linie[i + 1]:
                crescator = False

        if crescator:
            nr += 1

    return nr

def nrColoaneCuMinimCinci(matrice):
    latime = len(matrice[0])
    inatime = len(matrice)

    nr = 0

    for j in range(latime):
        min = matrice[0][j]
        for i in range(inatime):
            if matrice[i][j] < min:
                min = matrice[i][j]


        if min == 5:
            nr += 1

    return nr

def bubbleSort(linie):
    sortat = False

    while not sortat:
        sortat = True

        for i in range(len(linie) - 1):
            if linie[i] > linie[i + 1]:
                sortat = False

                aux = linie[i]
                linie[i] = linie[i + 1]
                linie[i + 1] = aux

def ordonareliniiBubbleSort(matrice):
    for linie in matrice:
        bubbleSort(linie)

if __name__ == '__main__':
    matrice = [[1, 6, 3],[4, 5, 4],[6, 7, 9]]

    ordonareliniiBubbleSort(matrice)

    print(matrice)

