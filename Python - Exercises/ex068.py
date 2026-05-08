from random import randint
print('==-' * 4)
print('Par ou Ímpar')
print('==-' * 4)
cont = 0
while True:
    computador = randint(1,10)
    n = int(input('Diga um número: '))
    parouimparjogador = input('Par ou Ímpar [P/I]? ').upper().replace(' ','')
    if (n + computador) % 2 == 0:
        parouimpar = 'P'
    else:
        parouimpar = 'I'
    if parouimpar == 'P':
        print('-=-')
        print(f'Você jogou {n} e o computador jogou {computador}. A soma é igual a {n + computador}, que é Par')
        print('-=-')
    else:
        print('-=-')
        print(f'Você jogou {n} e o computador jogou {computador}. A soma é igual a {n + computador}, que é Ímpar')
        print('-=-')
    if parouimparjogador[0] == parouimpar:
        print('Você ganhou!')
        cont += 1
    else:
        print('Você perdeu!')
        break
print(f'Você venceu {cont} vezes')