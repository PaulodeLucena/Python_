# Ler o nascimento de 7 pessoas e mostrar a quantidade de pessoas que são maiores e menores de idade

import datetime
atual = datetime.date.today().year
totalmaior = 0
totalmenor = 0

for pessoas in range(1, 8):
    nascimento = int(input("Em qual ano a {}° pessoas nasceu? ".format(pessoas)))
    idade = atual - nascimento

    if idade >= 18:
        totalmaior += 1
    else:
        totalmenor += 1

print('O número de pessoas maior de idade são {}'.format(totalmaior))
print('O número de pessoas menor de idade são {}'.format(totalmenor))

