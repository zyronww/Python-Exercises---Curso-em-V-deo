import random
name1 = input('Primeiro aluno: ')
name2 = input('Segundo aluno: ')
name3 = input('Terceiro aluno: ')
name4 = input('Quarto aluno: ')
lista = [name1, name2, name3, name4]
random.shuffle(lista)
print(f'''A ordem de apresentação será
{lista}''')