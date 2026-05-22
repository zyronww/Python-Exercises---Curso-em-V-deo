valores = list()
for c in range(0,5):
        valores.append(int(input(f'Digite o número que ficará na posição {c}: ')))
        n = valores[c]
        if c == 0:
            maior = n
            menor = n
        elif n > maior:
            maior = n
        elif n < menor:
            menor = n 
print('-' * 35)
print(f'Os valores digitados foram: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for c,v in enumerate(valores):
     if v == maior:
        print(f'{c}', end='...')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for c,v in enumerate(valores):
     if v == menor:
        print(f'{c}', end='...')