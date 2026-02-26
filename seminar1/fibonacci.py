
def fib(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

def fibNerecursiv(n):
    rez = [0, 1]
    for i in range(2, n):
        rez.append(rez[i - 1] + rez[i - 2])

    return rez

if __name__ == '__main__':

    print(fibNerecursiv(20))