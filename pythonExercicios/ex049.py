num = int(input('Digite o número da tabuada que você quer ver: '))
for n in range(1, 11):
    print('{} X {:2} = {}'.format(num, n, num*n))
