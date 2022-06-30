n1 = int(input('Digite um número: '))
total = 0
for x in range(1, n1 + 1):
    if n1 % x == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(x), end='')
print('\n\033[mO número {} foi divisivel {} vez'.format(n1, total))
if total == 2:
    print('O número é primo')
else:
    print('O número não é primo')
