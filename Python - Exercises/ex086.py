matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(0, 3):
    for a in range(0, 3):
        valor = int(input(f'\033[33mDigite um valor para a posição\033[m \033[36m[{c}, {a}]\033[m: '))
        matriz[c][a] = valor
print('-' * 40)
for c in range(0, 3):
    for a in range(0, 3):
        print(f'[ {matriz[c][a]} ] ',end='')
    print()