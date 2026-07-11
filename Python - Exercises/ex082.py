valores = []
valores_pares = []
valores_impares = []
escolha = ''
while escolha != 'N':
    n = int(input('Digite um valor: '))
    valores.append(n)
    escolha = input('Você quer continuar [S/N]? ').strip().upper().replace(' ','')
    while escolha not in 'SN':
        escolha = input('Você quer continuar [S/N]? ').strip().upper().replace(' ','')
    if n % 2 == 0:
        valores_pares.append(n)
    else:
        valores_impares.append(n)
print('-' * 30)
print(f'\033[33mA lista completa é: {valores}\033[m')
print(f'\033[36mA lista de valores pares é: {valores_pares}')
print(f'A lista de valores ímpares é: {valores_impares}\033[m')