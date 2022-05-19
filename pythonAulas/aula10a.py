n1 = float(input('Digite a primeira nota'))
n2 = float(input('Diite a segunda nota'))

media = (n1+n2) / 2

print('sua media foi {}'.format(media))

if media > 6.0:
    print('Você passou, parabens!')
else:
    print('Você reprovou, estude mais!')