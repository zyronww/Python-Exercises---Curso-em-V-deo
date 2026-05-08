print('10 primeiros termos de uma PA')
print('=' * 29)
priterm = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
nmutavel = priterm
contador = 1
while contador <= 10:
    print(f'{nmutavel} 🠖 ', end='')
    nmutavel += razao
    contador += 1
print('\033[33mFim\033[m')