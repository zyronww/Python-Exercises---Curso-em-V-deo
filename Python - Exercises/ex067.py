while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    print('='*33)
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('='*33)
print('-' * 21)
print('Tabuada v3 encerrada!')