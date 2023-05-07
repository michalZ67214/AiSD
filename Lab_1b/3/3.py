tab = [1, 2, 3, 11, 21, 111, 231]
print(tab)
    
for i in range(len(tab)):

  for j in range(0, len(tab) - i - 1):
    current_element = tab[j]
    next_element = tab[j + 1]

    if (int(str(current_element)[0]) > int(str(next_element)[0])) or ((int(str(current_element)[0]) == int(str(next_element)[0]) and current_element > next_element)):

      temp = tab[j]
      tab[j] = tab[j+1]
      tab[j+1] = temp

print(tab)