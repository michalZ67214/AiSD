tab = [-10, 1, 2, 8, 5]

x = int(input('Podaj x: '))

i = 0
while i < 5:
    if tab[i] == x:
        print(f'{x} jest w tablicy.')
    i += 1