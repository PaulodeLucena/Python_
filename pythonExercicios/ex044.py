print('-=' * 20)
print('Valor Produto')
print('-=' * 20)

produto = float(input('Digite o valor do produto: R$'))

print('Qual a forma de pagamento?')
pagamento = int(input('[1]à vista dinheiro/cheque: 10% de desconto \n[2]à vista no cartão: 5% de desconto'
                      ' \n[3]em até 2x no cartão: preço formal \n[4]3x ou mais no cartão: 20% de juros\n'))

if pagamento == 1:
    produto = produto - produto * (10 / 100)
    print('Você irá pagar R${:.2f}, você recebeu um desconto de 10%'.format(produto))
elif pagamento == 2:
    produto = produto - produto * (5 / 100)
    print('Você irá pagar R${:.2f},você recebeu um desconto de 5%'.format(produto))
elif pagamento == 3:
    print('Você irá pagar em até duas vezes no cartão, o valor é integral R${:.2f}'.format(produto))
elif pagamento == 4:
    produto = produto + produto * (20 / 100)
    print('Você irá pagar R${:.2f}, você irá pagar com juros de 20%'.format(produto))
else:
    print('Opção inválida')
