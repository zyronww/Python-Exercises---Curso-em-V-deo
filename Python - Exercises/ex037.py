n = int(input('Digite um número inteiro: '))
base = int(input((f'''Escolha uma das bases para a conversão:
[ 1 ] converter para \033[32mBinário\033[m
[ 2 ] converter para \033[32mHexadecimal\033[m
[ 3 ] converter para \033[32mOctal\033[m
Sua escolha: ''')))
if base == 1:
    print(f'O número \033[32m{n}\033[m covertido em binário é \033[33m{bin(n)[2:]}\033[m')
elif base == 2:
    print(f'O número \033[32m{n}\033[m covertido em Hexadecimal é \033[33m{hex(n)[2:]}\033[m')
elif base == 3:
    print(f'O número \033[32m{n}\033[m covertido em Octal é \033[33m{oct(n)[2:]}\033[m')
else:
    print('Erro 404. Resete o programa e tente novamente, digitando 1, 2 ou 3.')