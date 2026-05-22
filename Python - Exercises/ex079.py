numeros = list()
escolha = 0
while escolha != 'N':
    n = int(input(f'Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('O valor foi adicionado à lista!')
    else:
        print('O valor já está presente na lista e ele não será adicionado.')
    escolha = input('Quer continuar [S/N]? ').strip().upper()
    while escolha not in 'SN':
        escolha = input('Quer continuar [S/N]? ').strip().upper()
print('-' * 31)
numeros.sort()
print(f'Você digitou os valores {numeros}')  