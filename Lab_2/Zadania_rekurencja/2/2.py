def wynik(i):
    global licznik_wywolan
    licznik_wywolan += 1
    if i < 3:
        return 1
    else:
        if i % 2 == 0:
            return wynik(i-3) + wynik(i-1)+1
        else:
            return wynik(i-1) % 7

global licznik_wywolan
licznik_wywolan = 0
i = int(input('Podaj i: '))
print(f'wynik({i}): {wynik(i)}')
print(f'Ilość wywołań funkcji bez wywołania głownego: {licznik_wywolan-1}')