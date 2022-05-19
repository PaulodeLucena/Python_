velocidade = float(input('Qual a Velocidade do carro? '))

if velocidade <= 100.00:
    print('Tenha um bom dia, dirija com cuidado!')
else:
    multa = (velocidade - 100) * 7
    print('Multado! Você execeu o limite de velocidade permitido de 100Km/h \nA multa será de R${}'.format(multa))
    print('Tenha um bom dia, dirija com cuidado!')