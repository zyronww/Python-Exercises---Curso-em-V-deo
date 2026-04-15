from datetime import date
today = date.today().year
birth = int(input('Ano de Nascimento: '))
idade = today - birth
print(f'O atleta tem \033[32m{idade}\033[m anos.')
print('Classificação: ', end='')
if idade <= 9:
    print('\033[36mMirim\033[m')
elif 9 < idade <= 14:
    print('\033[36mInfantil\033[m')
elif 14 < idade <= 19:
    print('\033[36mJúnior\033[m')
elif 19 < idade <= 25:
    print('\033[36mSênior\033[m')
else:
    print('\033[36mMaster\033[m')