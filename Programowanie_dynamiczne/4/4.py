def dwumian(n_, m_):
    if n_ > m_:
        n = n_ + 1
    else:
        n = m_ + 1

    a = [[0] * n for i in range(n)]
    a[0][0] = -1
    for i in range(n):
        for j in range(n):
            if j  == 0 and j == i:
                a[i][j] = 1
            elif j >= 0 and i >= j:
                a[i][j] = a[i-1][j-1] + a[i-1][j]

    return a[n_][m_]

n = int(input('Podaj n: '))
m = int(input('Podaj m: '))
print(f'Współczynnik dwumianowy wynosi {dwumian(n, m)}')