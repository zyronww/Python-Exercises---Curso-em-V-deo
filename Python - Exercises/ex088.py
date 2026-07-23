from random import sample
from time import sleep
print('-'* 46)
print(f'{'MEGA SENA':^46}')
print('-'* 46)
jogos = []
numeros = []
quantidade = int(input('Quantos jogos você deseja que sejam sorteados? '))
for c in range(0, quantidade):
    numeros.append(sample(range(1, 60), 6))
    numeros[0].sort()
    jogos.append(numeros[0][:])
    numeros.clear()
print('=' * 7, f'Sorteando {quantidade} jogos', '=' * 7)
for c in range(0, quantidade):
    print(f'Jogo {c + 1}: {jogos[c]}')
    sleep(0.67)
print('=' * 10, 'Boa Sorte!!', '=' * 10)