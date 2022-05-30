salario = float(input('Digite seu salário: R$'))
if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Seu salário de R${:.2f} com aumento, será de R${:.2f}'.format(salario, novo))
