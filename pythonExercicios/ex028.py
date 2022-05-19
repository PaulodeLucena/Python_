import random
print('===' * 25)
print('Jogo da adivinhação, digite um número de 0 a 5 e veja se acertou!')
print('===' * 25)

computador = random.randint(0, 5)

escolha = int(input('Em que número pensei ? '))

if escolha == computador:
    print('Você acertou, pensamos no mesmo número {}'.format(computador))
else:
    print('Você  errou, eu pensei no número {} e não {}'.format(computador, escolha))






