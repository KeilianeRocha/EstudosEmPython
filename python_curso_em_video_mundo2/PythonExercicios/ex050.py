"""
REFAÇA O DESAFIO 009, MOSTRANDO A TABUADA DE UM NÚMERO QUE O USUÁRIO ESCOLHER, SO QUE AGORA UTILIZANDO UM LAÇO "FOR".
"""
numero = int(input('Insira um número para ver sua tabuada: '))
print('-'*12)
for c in range(1, 7):
    print('{} x {:2} = {}'.format(numero, c, numero*c))
