"""
ESCREVA UM PROGRAMA QUE LEIA DOIS NÚMEROS INTEIROS E COMPARE-OS, MOSTRANDO NA TELA UMA MENSAGEM:
- O PRIMEIRO VALOR É MAIOR
- O SEGUNDO VALOR É MAIOR
- NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS

"""

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO é \033[0;32mmaior\033[m')
elif n2 > n1:
    print('O SEGUNDO é \033[0;33mmaior\033[m')
else:
    print('Os números são \033[0;35miguais\033[m')
