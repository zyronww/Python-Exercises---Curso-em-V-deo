programacao = (
    'python',
    'java',
    'javascript',
    'algoritmo',
    'variável',
    'função',
    'loop',
    'tupla',
    'lista',
    'dicionário',
    'classe'
)
vogais = (
    'a',
    'e',
    'i',
    'o',
    'u'
)
for palavras in programacao:
    print(f'\nNa palavra \033[36m{palavras.capitalize()}\033[m temos: ', end='')
    for pos in range(0, len(palavras)):    
        if palavras[pos] in vogais or palavras[pos] in 'áàâãÁÀÂÃéèêẽÉÈÊíìîĩÍÌÎóòôõÓÒÔúùûũÚÙÛ':
            print(palavras[pos], end=' ')