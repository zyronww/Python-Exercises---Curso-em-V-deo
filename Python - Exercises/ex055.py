for c in range (1,6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi de \033[33m{maior:.1f}kg\033[m\ne o menor foi de \033[33m{menor:.1f}kg\033[m')