n = int(input('Digite a porção inteira de um número: '))
# Retorna as unidade, as dezenas, as centenas e os milhares do número digitado
unidade = n // 1 % 10
dezena = n // 10 % 10
centena = n // 100 % 10
milhar = n // 1000 % 10
# Mostra na tela as unidade, as dezenas, as centenas e os milhares do número digitado
print(f'Analisando o número {n}')
print('-'*10)
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')