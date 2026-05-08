print('-' * 30)
print('Casas Borabilladas'.center(30))
print('-' * 30)
tot = maisdemil = cont = 0
while True:
    cont += 1
    produto = input('Nome do produto: ').capitalize()
    preco = float(input('Preço do produto: R$'))
    tot += preco
    if preco > 1000:
        maisdemil += 1
    if cont == 1:
        maisbaratopreco = preco
        maisbaratonome = produto
    else:
        if preco < maisbaratopreco:
            maisbaratopreco = preco
            maisbaratonome = produto
    print('-' * 21)
    continuar = input('Quer continuar [S/N]? ').upper().replace(' ','')
    while continuar not in 'SN':
        continuar = input('Quer continuar [S/N]? ').upper().replace(' ','')
    print('-' * 21)
    if continuar == 'N':
        break
print('-' * 5, 'Fim do Programa', '-' * 5)
print(f'O total da compra foi \033[32mR${tot:.2f}\033[m')
if maisdemil == 1:
    print('Temos \033[36m1\033[m produto custando mais de \033[32mR$1000\033[m')
else:
    print('Temos \033[36m1\033[m produtos custando mais de \033[32mR$1000\033[m')
print(f'O produto mais barato foi \033[36m{maisbaratonome}\033[m e custou \033[32mR${maisbaratopreco:.2f}\033[m')