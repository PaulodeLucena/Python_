print('Valida palíndromo')
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverter = ''
for letra in range(len(junto) - 1, -1, -1):
    inverter = inverter + junto[letra]
if inverter == junto:
    print('é um palindromo')
else:
    print('Não é um palindromo')