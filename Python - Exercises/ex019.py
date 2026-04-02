import random
name1 = input('Primeiro aluno: ')
name2 = input('Segundo aluno: ')
name3 = input('Terceiro aluno: ')
name4 = input('Quarto aluno: ')
print(f'O aluno escolhido foi {random.choice((name1, name2, name3, name4))}')