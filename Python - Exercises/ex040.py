n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5:
    print(f'Com as notas {n1} e {n2}, a média será de {média} \nO aluno está \033[31mReprovado\033[m')
elif 5 <= média < 6.9:
    print(f'Com as notas {n1} e {n2}, a média será de {média} \nO aluno está \033[33mEm Recuperação\033[m')
else:
    print(f'Com as notas {n1} e {n2}, a média será de {média} \nO aluno está \033[32mAprovado\033[m')