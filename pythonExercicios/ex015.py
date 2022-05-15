print("Calculo de aluguel de carro")

dias = int(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos KM o carro rodou? '))

somadia = dias*60
somakm = km*0.15

valortotal = somakm + somadia

#alternativa mais facil: valortotal = (dias*60) + (km*0.15)

print('O valor total do aluguel do carro foi de: {:.2f}'.format(valortotal))