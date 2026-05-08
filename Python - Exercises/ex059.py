from time import sleep
n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
acao = int(input('''\033[33mOpções:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
--O que você deseja fazer?\033[m '''))
while acao != 5:
    if acao == 1:
        print(f'A soma entre {n1} e {n2} é igual a {n1+n2}')
    elif acao == 2:
        print(f'O produto de {n1} e {n2} é {n1*n2}')
    elif acao == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print(f'Os números digitados são iguais')
    elif acao == 4:
        print('Informe os números novamente:')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    print('\033[36m+==\033[m' * 9)
    sleep(0.8)    
    acao = int(input('''\033[33mOpções:
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa
--O que você deseja fazer?\033[m '''))
        