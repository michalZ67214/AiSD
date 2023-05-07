def tab_reverse(tab):
    if len(tab) == 0:
        return []
    else:
        return [tab.pop()] + tab_reverse(tab)

tab = [1, 2, 3, 4, 5]
print(tab)
print(tab_reverse(tab))