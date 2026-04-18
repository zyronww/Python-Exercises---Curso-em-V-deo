n = int(input('Digite um número inteiro: '))
primos = 0
for c in range(1, n + 1):
    if n % c == 0:
        print(f'\033[33m{c}\033[m', end=' ')
        primos += 1
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if primos == 1:
    print(f'\nO número {n} foi divisível \033[36m{primos} vez\033[m, ', end='')
else:
    print(f'\nO número {n} foi divisível \033[36m{primos} vezes\033[m, ', end='')
if primos == 2:
    print('por isso ele \033[32mé um número primo\033[m')
else:
    print('por isso ele \033[31mnão é um número primo\033[m')