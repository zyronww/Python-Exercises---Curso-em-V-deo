print('-'* 5, 'Lojas Feijão com Farinha', '-' * 5)
price = float(input('Qual foi o preço das compras? \033[32mR$\033[m'))
opção = int(input('''Formas de pagamento:
[ 1 ] à vista
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x no cartão
Qual é a sua escolha? '''))
if opção == 1:
    ajuste = price - price * ( 10 / 100 )
if opção == 2:
    ajuste = price - price * ( 5 / 100 )
if opção == 3:
    ajuste = price
if opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    ajuste = price + price * ( 20 / 100 )
    print(f'Sua compra parcelada em \033[33m{parcelas}x\033[m de \033[32mR${ajuste / parcelas:.2f}\033[m com juros de \033[36m20%\033[m')
print(f'Sua compra de \033[32mR${price:.2f}\033[m vai custar \033[32mR${ajuste:.2f}\033[m no final.')