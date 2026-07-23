matriz = [[0,0,0], [0,0,0], [0,0,0]]
pares = trccoluna = maiorseg = 0
for c in range(0, 3):
    for l in range(0, 3):
        valor = int(input(f'\033[33mDigite um valor para a posição\033[m \033[36m[{c}, {l}]\033[m: '))
        if valor % 2 == 0:
            pares += valor
        if l == 2:
            trccoluna += valor
        if c == 1:
            if l == 0:
                maiorseg = valor
            else:
                if valor > maiorseg:
                    maiorseg = valor
        matriz[c][l] = valor
print('-' * 40)
for c in range(0, 3):
    for l in range(0, 3):
        print(f'[ {matriz[c][l]} ] ',end='')
    print()
print('-' * 40)
print(f'\033[33mA soma de todos os valores pares é\033[m\033[32m {pares}\033[m'
f'\n\033[33mA soma dos valores da terceira coluna é\033[m\033[32m {trccoluna}\033[m'
f'\n\033[33mO maior valor da segunda linha é\033[m\033[32m {maiorseg}\033[m')
