from time import sleep; from random import randint
choice = int(input('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
O que você escolhe? '''))
computador = randint(1,3)
choice_ajusted = choice - 1
computer_ajusted = computador - 1
options = 'Pedra', 'Papel', 'Tesoura'
print('JO')
sleep(0.6)
print('KEN')
sleep(0.6)
print('POO!!!!!')
print('-=' * 12)
if str(choice) in '123':
    print(f'Computador jogou {options[computer_ajusted]}\nVocê jogou {options[choice_ajusted]}')
else:
    print(f'Computador jogou {options[computer_ajusted]}\nVocê jogou Nada')
print('-=' * 12)
if computador == 1:
    if choice == 1:
        print('Deu Empate')
    elif choice == 2:
        print('Você venceu!')
    elif choice == 3:
        print('Você perdeu')
    else:
        print('Perdeu aura pois não escolheu direito')
elif computador == 2:
    if choice == 2:
        print('Deu Empate')
    elif choice == 3:
        print('Você venceu!')
    elif choice == 1:
        print('Você perdeu')
    else:
        print('Perdeu aura pois não escolheu direito')
elif computador == 3:
    if choice == 3:
        print('Deu Empate')
    elif choice == 1:
        print('Você venceu!')
    elif choice == 2:
        print('Você perdeu')
    else:
        print('Perdeu aura pois não escolheu direito')