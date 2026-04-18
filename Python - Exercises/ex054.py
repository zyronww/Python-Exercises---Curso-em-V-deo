from datetime import date
maior = menor = 0
ano_atual = date.today().year
for c in range(1, 8):
    ano_nascimento = int(input(f'Em qual ano a {c}ª pessoa nasceu?'))
    idade = ano_atual - ano_nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print(f'No total, tivemos \033[36m{maior} pessoas maiores de idade\033[m\ne \033[33m{menor} pessoas menores de idade\033[m')