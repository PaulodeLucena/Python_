from datetime import date

print('Digite o ano de nascimento para saber sua categoria.')
ano = int(input('Nascimento:'))

atual = date.today().year
classificacao = atual - ano

if classificacao <= 9:
    print('Categoria Mirim')
elif classificacao <= 14:
    print('Categoria Infantil')
elif classificacao <= 19:
    print('Categoria Júnior')
elif classificacao <= 25:
    print('Categoria Sênior')
else:
    print('Categoria Master')
