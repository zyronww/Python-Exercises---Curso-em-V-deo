from datetime import date
year = int(input('Qual ano você gostaria de analisar? Digite "0" para analisar o ano atual: '))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f'O ano {year} é bissexto')
else:
    print(f'O ano {year} não é bissexto')