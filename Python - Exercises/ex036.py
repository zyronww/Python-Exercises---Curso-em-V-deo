valor = float(input('Valor da casa: \033[32mR$\033[m'))
salary = float(input('Salário do comprador: \033[32mR$\033[m'))
years = int(input('Quantos anos de financiamento? '))
prestação = valor / (years * 12)
mín = salary * 0.3 
print(f'Para pagar uma casa de \033[32mR${valor:.2f}\033[m em {years} anos a prestação será de \033[32mR${prestação:.2f}\033[m')
if prestação > mín:
    print('\033[31mEmpréstimo negado.\033[m')
else:
    print('\033[32mEmpréstimo concedido!\033[m')