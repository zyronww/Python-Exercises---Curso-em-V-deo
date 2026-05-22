produtos_precos = ('Lápis', 1.75, 'Piloto para Quadros', 7.99, 'Cartolina', 2, 'Fita isolante', 3.50, 'Mochila', 144.99, 'Caneta', 2.50, 'Pincel', 5, 'Canetinha', 3)
print('-' * 40)
print('Lista de Produtos'.center(40))
print('-' * 40)
for p, c in enumerate(produtos_precos):
    if p % 2 == 0:
        pontos = 32 - len(c)
        print(f'{c}', '.' * pontos, '\033[32mR$\033[m', end='')
    else:
        print(f'\033[32m{c:.2f}\033[m')
print('-' * 40)