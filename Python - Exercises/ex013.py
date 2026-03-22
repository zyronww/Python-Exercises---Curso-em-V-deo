salário = float(input('Qual é o salário do funcionário? '))
print(f'Um funcionário que ganhava R${salário:.2f}, com 15% de aumento, passa a receber R${salário + (salário * 15/100):.2f}')