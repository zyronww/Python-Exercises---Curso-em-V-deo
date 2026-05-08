termos = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
contador = 3
print(t1)
print(t2)
while contador != termos:
    contador += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print(t3)
print('FIMMM')
