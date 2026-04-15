weight = float(input('Qual é o seu peso? (kg) '))
height = float(input('Qual é a sua altura? (m) '))
imc = weight / height ** 2
print(f'O IMC dessa pessoa é {imc:.1f}')
print('Parabéns, você está na faixa de ', end='')
if imc <= 18.5:
    print('\033[36mAbaixo do Peso\033[m')
elif 18.5 < imc <= 25:
    print('\033[36mPeso Ideal\033[m')
elif 25 < imc <= 30:
    print('\033[36mSobrepeso\033[m')
elif 30 < imc <= 40:
    print('\033[36mObesidade\033[m')
else:
    print('\033[36mObesidade Mórbida\033[m')