escolha = ''
valores = list()
cont = 0
while escolha != 'N':
    n = int(input('Digite um valor: '))
    valores.append(n)
    escolha = input('Você quer continuar [S/N]? ').strip().upper().replace(' ','')
    while escolha not in 'SN':
        escolha = input('Você quer continuar [S/N]? ').strip().upper().replace(' ','')
    cont += 1
print('-' * 30)
valores.sort(reverse=True)
if cont == 1:
    print(f'\033[33mVocê digitou {cont} elemento.\033[m')
else:
    print(f'\033[33mVocê digitou {cont} elementos.\033[m')
print(f'Os valores em ordem decrescente são: {valores}')
if 5 in valores:
    print('\033[36mO valor 5 está presente na lista!\033[m')
else:
    print('\033[31mO valor 5 não está presente na lista.\033[m')