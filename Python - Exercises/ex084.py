pessoal = list()
pessoa = list()
maiorp = menorp = cont = 0
escolha = ''
while escolha != 'N':
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if cont == 0:
        maiorp = pessoa[1]
        menorp = pessoa[1]
    else:
        if pessoa[1] > maiorp:
            maiorp = pessoa[1]
        elif pessoa[1] < menorp:
            menorp = pessoa[1]
    pessoal.append(pessoa[:])
    pessoa.clear()
    escolha = input('Quer continuar [S/N]? ').replace(' ','').upper()
    while escolha not in 'SN':
        escolha = input('Quer continuar [S/N]? ').replace(' ','').upper()
    cont += 1
print(f'O maior peso foi de {maiorp:.1f}Kg. Esse foi o peso de: ', end='')        
for c in pessoal:
    if c[1] == maiorp:
        print(c[0], end='; ')
print(f'\nO menor peso foi de {menorp:.1f}Kg. Esse foi o peso de: ', end='') 
for c in pessoal:
    if c[1] == menorp:
        print(c[0], end='; ')
