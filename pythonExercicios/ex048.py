print('Soma de números impares (1 até 500)')
soma = 0
contador = 0
for n in range(1, 500, 2):
    if n % 3 == 0:
        contador = contador + 1
        soma = soma + n
print('A soma de todos os {} valores são {}'.format(contador, soma))
