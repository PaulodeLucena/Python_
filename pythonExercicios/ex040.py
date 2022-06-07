n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media > 7:
    print('Aluno foi aprovado, PARABENS!!')
elif 5 <= media and media <= 7:
    print('O aluno está em recuperação, ESTUDE!!!')
else:
    print('O aluno foi reprovado!!')
