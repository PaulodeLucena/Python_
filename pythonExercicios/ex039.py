from datetime import date
ano = int(input('Ano do seu nascimento: '))

atual = date.today().year
idade = atual - ano
alistar = ano + 18


print('Você tem aproximadamente {} anos'.format(idade))

if idade > 18:
    saldo = idade - 18
    print('Você precisa de alistar, o ano do seu alistamento foi: {}. Está atrasado {} anos'.format(alistar, saldo))
elif idade == 18:
    print('Você precisa se alistar, essa ano é seu alistamento')
else:
    saldo = 18 - idade
    print('Você precisará se alistar no ano de {}, você ainda tem {} anos até o ano do alistamento.'.format(alistar, saldo))