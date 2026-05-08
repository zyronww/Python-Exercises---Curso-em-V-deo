n = int(input('Digite um número inteiro para ver seu fatorial: '))
print('=' * 47)
nmutavel = n
fatorial = 1
print(f'\033[36m{n}!\033[m = ', end='')
while nmutavel > 0:
    if n == 1:
        print(end='') # Mostra, com a ajuda do último print, apenas que 1 fatorial é igual a 1
    elif nmutavel == 1:
        print(f'{nmutavel} = ', end='')
    else:
        print(f'{nmutavel} x ', end='')
    fatorial *= nmutavel
    nmutavel -= 1
print(f'\033[32m{fatorial}\033[m')   