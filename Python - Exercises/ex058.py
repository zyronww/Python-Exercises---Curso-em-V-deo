from random import randint; from time import sleep
ncomputador = randint(0,10)
sleep(0.8)
print('\033[36mSou seu computador. :)\033[m')
sleep(0.8)
print('\033[33mEu pensei em um número inteiro entre 0 e 10.\033[m')
sleep(0.8)
print('\033[36mTente adivinhá-lo!\033[m ')
tentativas = 0
sleep(0.8)
n = int(input('\033[33mQual número você acha que eu escolhi?\033[m'))
tentativas += 1
while n != ncomputador:
    if n > ncomputador:
        print('Menos...')
        tentativas += 1
    elif n < ncomputador:
        print('Mais...')
        tentativas += 1
    n = int(input('\033[33mQual número você acha que eu escolhi?\033[m'))
if tentativas == 1:
    print(f'Você acertou com \033[33m{tentativas} tentativa.\033[m Boa!')
else:
    print(f'Você acertou com \033[33m{tentativas} tentativas.\033[m Boa!')       