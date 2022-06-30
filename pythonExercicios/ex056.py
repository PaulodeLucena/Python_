somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
somamulher20 = 0

for pessoas in range(1, 5):
    print('-----------{}° Pessoa-------------'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if idade > maioridadehomem and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        somamulher20 += 1

mediaidade = somaidade / 4

print('A média de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadehomem, nomevelho))
print('Na lista digitada, tem {} mulher com menos de 20 anos'.format(somamulher20))
