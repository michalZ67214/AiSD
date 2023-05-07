def silnia(n):
    if n == 0:
        s = 1
    else:
        s = silnia(n-1) * n
    return s

n = int(input('Podaj n: '))

while n <= 0:
    print()
    n = int(input('Podaj n: '))

print(f'Silnia z {n} wynosi: {silnia(n)}')