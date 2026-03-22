days = int(input('Total de dias alugados: '))
km = float(input('Total de quilômetros rodados: '))
preço_dias = days * 60
preço_km = km * 0.15
print(f'O valor final é R${preço_dias + preço_km:.2f}')