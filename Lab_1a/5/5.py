tab = [[3, 2, 5], [-5, 8, -10], [4, -2, 15]]
print(tab)

i = 0
while i < len(tab):
    wiersz_min = tab[i][0]
    min_poz = 0
    j = 1
    while j < len(tab[i]):
        if tab[i][j] < wiersz_min:
            wiersz_min = tab[i][j]
            min_poz = j
        j += 1
    temp = tab[i][0]
    tab[i][0] = tab[i][min_poz]
    tab[i][min_poz] = temp
    i += 1

print(tab)