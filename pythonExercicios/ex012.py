print("Desconto de 5% nos produtos")

n1 = float(input("Digite o valor do produto: R$"))

produtodesc = n1 - (n1*5/100)

print('O valor do produto com 5% de desconto é de {:.2f}'.format(produtodesc))