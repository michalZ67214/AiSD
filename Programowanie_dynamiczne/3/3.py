def S(n):
    if n == 0: return 1
    elif n == 1: return 1
    elif n>1:
        s = [1, 1]
        i = 2
        while(i<=n):
            s.append((2*s[i-1])-s[i-2])
            i += 1
            
    return s[i-1]
    
n = int(input('Podaj n: '))
if n>=0: print(S(n))
else: print('Podano zły argument')