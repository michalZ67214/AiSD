tab = [10, 7, -5, 8, 5]

minimalna = tab[0]

i = 1
while i < len(tab):
    if tab[i] < minimalna:
        minimalna = tab[i]
    i += 1

print(f'Wartość minimalna tablicy: {minimalna}')