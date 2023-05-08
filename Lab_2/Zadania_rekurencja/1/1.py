# wersja 1 ##############################################

# iteracyjnie
def NWD_1_i(a,b):
    while a!=b:
        if a>b: a = a-b
        else: b = b-a
    return a

# rekurencyjnie
def NWD_1_r(a,b):
    if a!=b:
        if a>b: return NWD_1_r(a-b, b)
        else: return NWD_1_r(a, b-a)
    return a




# wersja 2 ###############################################

# iteracyjnie
def NWD_2_i(a,b):
    while b!=0:
        temp = b
        b = a%b
        a = temp
    return a

# rekurencyjnie
def NWD_2_r(a,b):
    if b!=0:
        return NWD_2_r(b, a%b)
    return a


wersja = input('Wybierz wersję algorytmu NWD(1/2): ')
forma = input('Wybierz formę algorytmu NWD, iteracyjną lub rekurencyjną (i/r): ')
a = int(input('Podaj a: '))
b = int(input('Podaj b: '))

if wersja == '1' and forma == 'i':
    print(NWD_1_i(a, b))
elif wersja == '1' and forma == 'r':
    print(NWD_1_r(a, b))
elif wersja == '2' and forma == 'i':
    print(NWD_2_i(a, b))
elif wersja == '2' and forma == 'r':
    print(NWD_2_r(a, b))
else:
    print('Nieprawidłowa wersja lub forma')