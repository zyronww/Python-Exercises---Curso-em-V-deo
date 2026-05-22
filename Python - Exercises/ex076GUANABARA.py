listagem = ('Lápis', 1.75, 'Piloto para Quadros', 7.99, 'Cartolina', 2, 'Fita isolante', 3.50, 'Mochila', 144.99, 'Caneta', 2.50, 'Pincel', 5, 'Canetinha', 3)
print('-' * 40)
print(f'{'Listagem de Preços':^40}')
print('-' * 40)
for pos in range (0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)