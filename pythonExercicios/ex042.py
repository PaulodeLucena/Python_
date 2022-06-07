print('-='*20)
print('Analisa triangulo')
print('-='*20)
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triângulo ', end='')
    if r1 == r2 and r2 == r3:
        print('Equilátero')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Escaleno')
    else:
        print('Isóceles')
else:
    print('Os segmentos acima não podem formar um triângulo')

