nome = str(input('Qual seu nome? ')).upper()
if nome == 'PAULO':
    print('Nome bonito!')
elif nome == 'JOÃO' or nome == 'MARIA' or nome == 'PEDRO':
    print('Seu nome é bom popular aqui no brasil !')
else:
    print('Seu nome é bem normal')
print('Tenha um bom dia {}'.format(nome))
