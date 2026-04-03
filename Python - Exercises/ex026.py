phrase = input('Digite uma frase: ').strip().lower()
print(f'A letra "A" aparece {phrase.count('a')} vezes na frase digitada.')
print(f'A primeira letra "A" apareceu na posição {phrase.find('a') + 1}')
print(f'A última letra "A" apareceu na posição {phrase.rfind('a') + 1}')