"""
CRIE UM PROGRAMA  QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA SE ELE É 'PAR' OU 'ÍMPAR';

"""

n = int(input('Digite um número: '))
resultado = n % 2
# print('O resultado foi: {}'.format(resultado))

if resultado == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número é ÍMPAR'.format(n))