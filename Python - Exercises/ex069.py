maiorque18 = homem = mulhermenosde20 = 0
while True:
    print('-' * 19)
    print('Cadastre uma Pessoa')
    print('-' * 19)
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().replace(' ','')
    if idade > 18:
        maiorque18 += 1
    if sexo[0] == 'M':
        homem += 1
    if idade < 20 and sexo[0] == 'F':
        mulhermenosde20 += 1
    print('=' * 21)
    continuar = input('Quer continuar [S/N]? ').upper().replace(' ','')
    print('=' * 21)
    while continuar not in 'SN':
        print('=' * 21)
        continuar = input('Quer continuar [S/N]? ').upper().replace(' ','')
        print('=' * 21)
    if continuar == 'N':
        break
if maiorque18 == 1:
    print(f'Ao todo, temos {maiorque18} pessoa com idade maior que 18')
else:
    print(f'Ao todo, temos {maiorque18} pessoas com idade maior que 18')
if homem == 1:
    print(f'Temos {homem} homem cadastrado')
else:
    print(f'Temos {homem} homens cadastrados')
if mulhermenosde20 == 1:
    print(f'E temos {mulhermenosde20} mulher com menos de 20 anos')
else:
    print(f'E temos {mulhermenosde20} mulheres com menos de 20 anos')