from random import randint
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os valores sorteados foram: ', end='')
for c in n:
    print(f'\033[36m{c}\033[m', end=' ')
ordenado = sorted(n)
print(f'\nO maior valor foi \033[32m{ordenado[-1]}\033[m')
print(f'O menor valor foi \033[33m{ordenado[0]}\033[m')