largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

area = largura*altura

print('Sua parede com a dimensão de {}x{}, tem o total de {:.2f}m²'.format(largura, altura, area))

tinta = area / 2

print('A quantida de tinta para pintar essa parede é de {:.2f}L'.format(tinta))