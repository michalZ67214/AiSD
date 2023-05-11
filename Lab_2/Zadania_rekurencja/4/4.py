from math import floor

def _10_na_2_(a, b):
    if a == 0:
        if b == '':
            return 0
        else:
            return b
    else:
        cyfra_dwojkowa = a % 2
        a = floor(a / 2)
        return _10_na_2_(a, str(cyfra_dwojkowa)+b)

a = int(input('Podaj liczbę dziesiętną: '))
dwojkowa = _10_na_2_(a, '')
print(f'{a} jako liczba dwójkowa to {dwojkowa}')