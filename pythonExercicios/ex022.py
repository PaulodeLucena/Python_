nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome... ')

#maiuscula = nome.upper()
print('seu nome completo em letra maiuscula é {}'.format(nome.upper()))

#minuscula = nome.lower()
print('seu nome completo em letra minuscula é: {}'.format(nome.lower()))

print('Seu nome tem {} de letras.'.format(len(nome) - nome.count(' ')))

# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))