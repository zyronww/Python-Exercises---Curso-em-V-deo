print('-'*22)
print('Sequência de Fibonacci')
print('-'*22)
quantidade = int(input('Quantos termos você deseja mostrar? '))
print('-'*35)
n1 = contador = 0
n2 = 1
while contador != quantidade:
    if contador != quantidade:
        if contador == 0:
            print(f'{n1} 🠖 ', end = '')
            contador += 1
        else:
            n1 = n1 + n2
            print(f'{n1} 🠖 ', end = '')
            contador += 1
    if contador != quantidade:
        n2 = n2 + n1
        print(f'{n2} 🠖 ', end = '')
        contador += 1
print('Fim')