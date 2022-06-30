a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
resto_a  = a % 2
resto_b =  b % 2
if resto_a == 0 or resto_b == 0:
    print('foi digitado um número par')
else:
    print('Não foi digitado número par')