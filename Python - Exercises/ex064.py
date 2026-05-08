soma = cont = n = 0
while n != 999:
    n = float(input('Digite um número [999 para parar]: '))
    if n != 999:
        cont += 1
        soma += n
print(f'\033[33mVocê digitou {cont} números e a soma entre eles foi {soma}\033[m')