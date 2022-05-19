# importação que puxa a data atual do computador
from datetime import date

print('Ano bissexto')

# escolha do ano
ano = int(input('Qual ano você quer analisar? Digite 0 caso queira analisar o ano atual: '))

# condição do ano
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))
