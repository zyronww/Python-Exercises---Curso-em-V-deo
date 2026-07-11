expressao = input('Digite uma expressão: ')
lista = []
for c in expressao:
    lista.append(c)
abre = fecha = 0
for c in expressao:
    if c == '(':
        abre += 1
    elif c == ')' and abre > fecha:
        fecha += 1
if fecha == abre:
    print('\033[36mA expressão digitada é válida!\033[m')
else:
    print('\033[31mA expressão digitada é inválida!\033[m') 