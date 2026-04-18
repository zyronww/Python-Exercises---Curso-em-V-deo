soma = quantidade = 0
for c in range (1, 501, 2):
    if c % 3 == 0:
        soma += c
        quantidade += 1
print(f'A soma de todos os \033[32m{quantidade}\033[m números é igual a \033[36m{soma}\033[m')