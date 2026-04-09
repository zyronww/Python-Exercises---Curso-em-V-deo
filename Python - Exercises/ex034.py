salary = float(input('Salário: \033[32mR$\033[m'))
if salary <= 1250:
    print(f'O salário de \033[32mR${salary:.2f}\033[m teve um aumento de \033[33m15%\033[m e agora é de \033[32mR${salary + salary * 0.15:.2f}\033[m')
else:
    print(f'O salário de \033[32mR${salary:.2f}\033[m teve um aumento de \033[33m10%\033[m e agora é de \033[32mR${salary + salary * 0.10:.2f}\033[m')