numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print('-' * 26)
print(f'Você digitou os valores {numeros}')
print('-' * 26)
if numeros.count(9) == 1:
    print(f'O valor 9 apareceu {numeros.count(9)} vez')
else:
    print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if numeros.count(3) > 0:
    print(f'O valor 3 apareceu pela primeira vez na {numeros.index(3)}ª posição')
else:
    print('O valor 3 não apareceu nenhuma vez')
cont = 0
print('Os valores pares digitados foram ', end='')
for p in numeros:
    if p % 2 == 0:
        print(f'\033[36m{p}\033[m', end=' ')
    else:
        cont += 1
    if cont == 4:
        print('\033[31NENHUM\033[m')   