escolha = ''
cont = nsomados = 0
while escolha != 'N':
    cont += 1
    n = float(input('Digite um número: '))
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    nsomados += n
    escolha = input('Você quer continuar [S/N]? ').upper().replace(' ', '')
    while escolha not in 'SN':
        escolha = input('Você quer continuar [S/N]? ').upper().replace(' ', '')
media = nsomados / cont
if cont == 1:
    print(f'\033[33mVocê digitou {cont} número e a média foi {media:.2f}\033m')
else:
    print(f'\033[33mVocê digitou {cont} números e a média foi {media:.2f}\033m')
print(f'\033[36mO maior valor foi {maior} e o menor foi {menor}\033[m')
