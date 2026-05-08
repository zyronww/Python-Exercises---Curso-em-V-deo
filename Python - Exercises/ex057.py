sexo = input('Informe seu sexo [M/F]: ').upper().replace(' ', '')
while sexo not in 'MF':
    sexo = input('\033[31mDados inválidos.\033[m \033[33mDigite "M" se seu sexo for masculino e "F" se for feminino:\033[m').upper().replace(' ', '')
if sexo == 'M':
    print('Sexo masculino registrado com sucesso!')
elif sexo == 'F':
    print('Sexo feminino registrado com sucesso!')