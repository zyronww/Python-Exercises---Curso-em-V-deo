from datetime import date
year = int(input('Ano de nascimento da pessoa: '))
anoatual = date.today().year
idade =  anoatual - year
tempo_alistamento = 18 - idade
if idade < 18:
    print(f'A pessoa que nasceu em \033[33m{year}\033[m tem \033[32m{idade}\033[m anos de idade em \033[34m{anoatual}\033[m. \nEla deverá se alistar em \033[32m{tempo_alistamento}\033[m anos, ou seja, em \033[34m{anoatual + tempo_alistamento}\033[m')
elif idade == 18:
    print(f'A pessoa que nasceu em \033[33m{year}\033[m tem \033[32m{idade}\033[m anos de idade em \033[34m{anoatual}\033[m. \nEla deverá se \033[31mImediatamente\033[m')
else:
    tempo_alistamento = idade - 18
    print(f'A pessoa que nasceu em \033[33m{year}\033[m tem \033[32m{idade}\033[m anos de idade em \033[34m{anoatual}\033[m. \nEla deveria ter se alistado ou já se alistou há \033[32m{idade - 18}\033[m anos, ou seja, em \033[34m{anoatual - tempo_alistamento}\033[m ')