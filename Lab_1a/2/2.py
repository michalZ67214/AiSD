n = int(input('Podaj n: '))

while n <= 0:
    print()
    n = int(input('Podaj n: '))

ile_u = 0

i=0
while i < n:
    ai = int(input(f'Podaj liczbę nr {i+1}: '))
    if ai < 0:
        ile_u += 1
    i += 1

print(f'Ilość wczytanych liczb ujemnych: {ile_u}')