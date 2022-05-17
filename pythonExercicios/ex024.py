print('O nome da cidade que você nasceu começa com Santo(s)? Validados abaixo')

cidade = str(input("Digite a cidade que nasceu: ")).strip()

print(cidade[:5].upper() == 'SANTO')