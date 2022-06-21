primeiro = int(input('Digite, o elemento inicial de uma PA(número): '))
razao = int(input('Digite o número da razão: '))
ultimo = primeiro + (10 - 1) * razao

for c in range(primeiro, ultimo, razao):
    print('{}'.format(c), end=' > ')
print('Fim')