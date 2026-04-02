from math import hypot
catoposto = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))
print(f'{hypot(catoposto, catadj):.2f}')