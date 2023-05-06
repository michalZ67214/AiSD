from math import sqrt

a = int(input('Podaj a: '))
b = int(input('Podaj b: '))
c = int(input('Podaj c: '))

while a == 0:
    print()
    a = int(input('Podaj a: '))
    b = int(input('Podaj b: '))
    c = int(input('Podaj c: '))

d = (b ** 2) - (4 * a * c)

if d >= 0:
    if d == 0:
        x0 = (-b) / (2 * a)
        print(f'Rozwiązanie:\nx0 = {x0}')
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print(f'Rozwiązania:\nx1 = {x1}\nx2 = {x2}')
else:
    print('Brak rozwiązań')