print('Média do aluno bimestres')

n1 = int(input('Primeiro bimestre: '))
n2 = int(input('Segundo bimestre: '))
n3 = int(input('Terceiro bimestre: '))
n4 = int(input('Quarto bimestre: '))
media = (n1+n2+n3+n3) / 4

if n1 <= 10 and n2 <= 10 and n3 <= 10 and n4 <= 10:
    print('A média do aluno foi {}'.format(media))
else:
    print('Alguma nota nota foi digitada incorretamente, coloque entre 0 e 10')