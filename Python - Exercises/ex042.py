print('-=-' * 8, '67', '-=-' * 8, '67')
print('\033[35mAnalisador de Triângulos 2.0 atualizado 2026 by zyron 67\033[m')
print('-=-' * 8, '67', '-=-' * 8, '67')
a = float(input('\033[32mPrimeiro Segmento:\033[m '))
b = float(input('\033[32mSegundo Segmento:\033[m '))
c = float(input('\033[32mTerceiro Segmento:\033[m '))
print('-' * 49)
if a + b > c and b + c > a and c + a > b:
    if a == b == c:
        print('Os segmentos \033[32mpodem\033[m formar um \033[36mtriângulo equilátero\033[m')
    elif a == b != c or a == c != b or c == b != a:
        print('Os segmentos \033[32mpodem\033[m formar um \033[36mtriângulo isósceles\033[m')
    elif a != b and a != c and b != c:
        print('Os segmentos \033[32mpodem\033[m formar um \033[36mtriângulo escaleno\033[m')
else:
    print('Os segmentos \033[31mnão podem\033[m formar um triângulo')