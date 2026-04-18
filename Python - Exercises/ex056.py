somaidades = hmaisvelho = maisvelho = mulhermenos20 = 0
for c in range (1, 5):
    print('_'*5,f'{c}ª Pessoa', '_'*5)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    if c == 1:
        maisvelho = idade
    else:
        if idade > maisvelho:
            maisvelho = idade
    somaidades += idade
    sexo = input('Sexo [M/F]: ').upper()
    if sexo == 'M' and idade == maisvelho:
        hmaisvelho = idade
        nomemaisvelho = nome
    if sexo == 'F' and idade < 20:
        mulhermenos20 += 1
    if sexo not in 'MF':
        print('Digite "M" ou "F" na próxima vez')
média = somaidades / c
print(f'A média de idade do grupo é de {média} anos')
print(f'O homem mais velho tem {hmaisvelho} anos e se chama {nomemaisvelho}.')
if mulhermenos20 == 1:
    print(f'Ao todo é {mulhermenos20} mulher com menos de 20 anos.')
else:
    print(f'Ao todo são {mulhermenos20} mulheres com menos de 20 anos.')