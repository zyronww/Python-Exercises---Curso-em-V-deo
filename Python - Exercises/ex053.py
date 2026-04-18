frase = input('Digite uma frase: ').replace(' ','').upper()
inverso = ''
for c in frase[::-1]:
    inverso += c
if inverso == frase:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')