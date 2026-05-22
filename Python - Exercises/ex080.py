valores = list()
for c in range(0,5):
    v = int(input('Digite um valor: '))
    if c == 0:
        valores.append(v)
        print(f'O valor {v} foi adicionado ao final da lista')
    elif v >= valores[-1]:
        valores.append(v)
        print(f'O valor {v} foi adicionado à posição {len(valores) - 1} (final)')
    else:
        pos = 0
        while pos < len(valores):
            if v <= valores[pos]:
                valores.insert(pos, v)
                print(f'O valor {v} foi adicionado à posição {len(valores) - 1}')
                break
            pos += 1
print(f'Os valores ordenados da lista são: {valores}')