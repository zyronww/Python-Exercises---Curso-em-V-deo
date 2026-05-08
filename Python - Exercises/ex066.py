soma = cont = 0
while True:
    n = float(input('Digite um valor (999 para parar): '))
    if n != 999:
        soma += n
    cont += 1
    if n == 999:
        break
print(f'A soma dos \033[36m{cont}\033[m números é igual a \033[32m{soma}\033[m')