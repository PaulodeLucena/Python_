import math

# longo

'''catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))

hiponetusa = (catetooposto ** 2 + catetoadjacente ** 2) ** (1/2)

print('O valor da hipotenusa é igual a {:.2f}'.format(hiponetusa))'''


# simples

catetooposto = float(input('Digite o comprimento do cateto oposto: '))
catetoadjacente = float(input('Digite o comprimento do cateto adjacente: '))

hiponetusa = math.hypot(catetooposto, catetoadjacente)

print('O valor da hipotenusa é igual a {:.2f}'.format(hiponetusa))