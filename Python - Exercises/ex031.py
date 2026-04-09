distance = float(input('Distância da viagem: '))
if distance <= 200:
    price = distance * 0.5
    print(f'Sua viagem de \033[34m{distance}km\033[m custará um total de \033[32mR${price:.2f}\033[m.')
else:
    price = distance * 0.45
    print(f'Sua viagem de \033[34m{distance}km\033[m custará um total de \033[32mR${price:.2f}\033[m.')