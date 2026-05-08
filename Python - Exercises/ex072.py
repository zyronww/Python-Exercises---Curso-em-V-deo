n_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número inteiro entre 0 e 20: '))
while n < 0 or n > 20:
    n = int(input('Tente outra vez. Digite um número inteiro entre 0 e 20: '))
print(f'Você digitou o número "\033[36m{n_extenso[n]}\033[m"')