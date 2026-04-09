velocity = float(input('Velocidade atual do carro: '))
if velocity > 80:
    multa = (velocity - 80) * 7
    print(f'\033[31;1mVocê receberá uma multa de \033[33mR${multa:.2f}\033[m\033[31;1m, pois ultrapassou em \n{velocity - 80} quilômetros por hora do permitido, que é 80km/h\033[m')
    print(f'\033[32mTenha um bom dia e dirija com mais cuidado!\033[m')
else:
    print(f'\033[32mTenha um bom dia e dirija com segurança!\033[m')