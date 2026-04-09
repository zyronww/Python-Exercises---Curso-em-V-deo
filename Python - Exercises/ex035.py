print('-=-' * 8, '67', '-=-' * 8)
print('\033[35mAnalisador de Triângulos atualizado 2026 by zyron 67\033[m')
print('-=-' * 8, '67', '-=-' * 8)
a = float(input('\033[32mPrimeiro Segmento:\033[m '))
b = float(input('\033[32mSegundo Segmento:\033[m '))
c = float(input('\033[32mTerceiro Segmento:\033[m '))
print('-' * 38)
if a + b > c and b + c > a and c + a > b:
    print('Os segmentos \033[32mpodem\033[m formar um triângulo')
else:
    print('Os segmentos \033[31mnão podem\033[m formar um triângulo')