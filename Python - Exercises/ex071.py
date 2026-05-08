print('-' * 30)
print('Banco Borabillado'.center(30))
print('-' * 30)
ced50 = 50
ced20 = 20
ced10 = 10
ced1 = 1
cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Qual valor você quer sacar? R$'))
while True:
    while valor >= 50:
        valor -= ced50
        cont50 += 1
    while valor >= 20:
        valor -= ced20
        cont20 += 1
    while valor >= 10:
        valor -= ced10
        cont10 += 1
    while valor >= 1:
        valor -= ced1
        cont1 += 1
    if valor == 0:
        break
if cont50 != 0:
    if cont50 == 1:
        print(f'Total de \033[36m{cont50}\033[m cédula de \033[32mR$50\033[m')
    else:
        print(f'Total de \033[36m{cont50}\033[m cédulas de \033[32mR$50\033[m')
if cont20 != 0:
    if cont20 == 1:
        print(f'Total de \033[36m{cont20}\033[m cédula de \033[32mR$20\033[m')
    else:
        print(f'Total de \033[36m{cont20}\033[m cédulas de \033[32mR$20\033[m')
if cont10 != 0:
    if cont10 == 1:
        print(f'Total de \033[36m{cont10}\033[m cédula de \033[32mR$10\033[m')
    else:
        print(f'Total de \033[36m{cont10}\033[m cédulas de \033[32mR$10\033[m')
if cont1 != 0:
    if cont1 == 1:
        print(f'Total de \033[36m{cont1}\033[m cédula de \033[32mR$1\033[m')
    else:
        print(f'Total de \033[36m{cont1}\033[m cédulas de \033[32mR$1\033[m')
print('-' * 52)
print('\033[33mVolte sempre ao Banco Borabillado.\033[m \033[36mTenha um bom dia!\033[m')