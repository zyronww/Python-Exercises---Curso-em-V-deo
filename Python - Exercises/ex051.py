print('-'* 40)
print(f'{'10 Primeiros Termos de uma PA':^40}')
print('-'* 40)
primeiro_termo = int(input('Primeiro Termo: '))
razão = int(input('Razão: '))
ultimo_termo = primeiro_termo + ( 10 - 1 ) * razão + razão
for c in range (primeiro_termo, ultimo_termo, razão):
    print(c, end=' 🠖 ')
print('\033[33mAcabou\033[m')