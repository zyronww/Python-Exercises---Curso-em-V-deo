n = int(input('Digite a porção inteira de um número: '))
n = str(n)
# Mostra na tela as unidade, as dezenas, as centenas e os milhares do número digitado
print(f'Analisando o número {n}')
print('-'*10)
print(f'Unidade: {n[-1]}')
print(f'Dezena: {n[-2]}')
print(f'Centena: {n[-3]}')
print(f'Milhar: {n[-4]}')