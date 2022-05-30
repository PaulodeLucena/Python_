print('-='* 20)
print('Conversor')
print('-='* 20)

n = int(input('Digite um número inteiro: '))

select = int(input('Escolha um número para converter \n[1]Binário\n[2]Octal\n[3]Hexadecimal\n'))


if select == 1:
    print('O número convertido para binário fica {}'.format(bin(n)[2:]))
elif select == 2:
    print('O número convertido fica octal fica {}'.format(oct(n)[2:]))
elif select == 3:
    print('O número convertido para hexadecimal fica {}'.format(hex(n)[2:]))
else:
    print('Opção invalida.')