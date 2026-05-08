print('MEGA PA')
print('=' * 7)
priterm = int(input('Primeiro Termo da PA: '))
razao = int(input('Razão da PA: '))
c = priterm
contador = 0
df = 1
escolha = 11
while escolha != 0:
    while df <= escolha:
        contador += 1
        print(f'{c} 🠖 ', end='')
        c += razao
        df += 1
        if df == escolha:
            df = 1
            print('\033[33mPausa\033[m')
            escolha = int(input('Quantos termos a mais da PA você deseja ver? '))
            if escolha != 0:
                escolha += 1
print(f'\033[36mA PA foi finalizada com {contador} termos exibidos.\033[m')