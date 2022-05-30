print('-='*20)
print('Emprestimo')
print('-='*20)

casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
anos = int(input('Em quantos anos você vai pagar? '))
prestacao = casa / (anos * 12)

print('para pagar a casa de {:.2f} em {} anos,'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao >= salario * (30 / 100):
    print('Emprestimo negado.')
else:
    print('Emprestimo aprovado.')