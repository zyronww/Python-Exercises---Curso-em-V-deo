l1 = []
while True:
    nome = input('Nome: ')
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    l1.append([nome, [n1, n2], media])
    escolha = input('Quer continuar [S/N]? ').strip()
    while escolha not in 'NnSs':
        escolha = input('Quer continuar [S/N]? ').strip()
    if escolha in 'Nn':
        break
print('=' * 30)
print('N°  Nome        Média')
print('-' * 30)
for c, v in enumerate(l1):
    print(f'{c}   {l1[c][0]}', end = '')
    print(f'{l1[c][2]:>12}')
print('-' * 30)
while True:
    aluno = int(input('Mostrar as notas de qual aluno? [999 para interromper]: '))
    if aluno == 999:
        break
    print(f'\033[33mAs notas de \033[36m{l1[aluno][0]}\033[m \033[33msão\033[m \033[36m{l1[aluno][1]}\033[m')
    print('-' * 30)