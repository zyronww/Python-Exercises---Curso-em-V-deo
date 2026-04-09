n = int(input('Digite um número inteiro: '))
if n % 2 == 0:
    print(f'{n} é \033[34mpar\033[m.')
else:
    print(f'{n} é \033[1;31mímpar\033[m.')