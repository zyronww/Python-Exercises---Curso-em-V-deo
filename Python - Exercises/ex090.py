aluno = dict()
aluno['nome'] = input('Nome: ')
aluno['média'] = float(input(f'Média de {aluno['nome']}: '))
if aluno['média'] < 6:
    aluno['situação'] = '\033[31mReprovado\033[m'
else:
    aluno['situação'] = '\033[32mAprovado\033[m'
print('-' * 15)
print(f'O nome é {aluno['nome']}')
print(f'A média de {aluno['nome']} é igual a {aluno['média']}')
print(f'A situação de {aluno['nome']} é {aluno['situação']}')