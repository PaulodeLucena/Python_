import random
import time
print('===' * 25)
print('Pedra, Papel, Tesoura')
print('===' * 25)

itens = ('Pedra', 'Papel', 'Tesoura')
computador  = random.randint(0, 2)
escolha = int(input('Escolha uma opção: \n[0]Pedra\n[1]Papel\n[2]Tesoura\nQual sua jogada? '))
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
time.sleep(1)

print('===' * 25)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[escolha]))
print('===' * 25)

if computador == 0:
    if escolha == 0:
        print("Empate")
    elif escolha == 1:
        print("O jogador ganhou")
    elif escolha == 2:
        print('O jogador perdeu')
    else:
        print('Escolha inválida')
elif computador == 1:
    if escolha == 0:
        print('O jogador perdeu')
    elif escolha == 1:
        print('Empate')
    elif escolha == 2:
        print('O jogador ganhou')
    else:
        print('Escolha inválida')
elif computador == 2:
    if escolha == 0:
        print('O jogador ganhou')
    elif escolha == 1:
        print('O jogador perdeu')
    elif escolha == 2:
        print('Empate')
    else:
        print('Escolha inválida')
