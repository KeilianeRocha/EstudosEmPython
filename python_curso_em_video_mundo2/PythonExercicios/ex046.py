"""
CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

"""
import time
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^40}'.format('JOKENPÔ'))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('='*30)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('='*30)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    if jogador == 1:
        print('Jogador VENCE')
    if jogador == 2:
        print('Jogador PERDEU')
elif computador == 1:
    if jogador == 1:
        print('EMPATE!')
    if jogador == 2:
        print('Jogador PERDEU')
    if jogador == 0:
        print('Jogador VENCE')
elif computador == 2:
        if jogador == 2:
            print('EMPATE!')
        if jogador == 0:
            print('Jogador VENCE')
        if jogador == 1:
            print('Jogador PERDEU')
else:
    print('Jogada inválida! Tente novamente')
print('{:=^40}'.format('PRESS ENTER Para jogar novamente'))

