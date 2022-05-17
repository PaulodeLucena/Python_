nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()

print('Muito prazer em conhecer-lo! \nSeu primeiro nome é {}. \nSeu ultimo nome é {}.'.format(n[0], n[len(n)-1]))