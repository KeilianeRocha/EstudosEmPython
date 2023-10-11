"""
MELHORE O JOGO DO DESAFIO 029 ONDE O COMPUTADOR VAI "PENSAR" EM UM NUMERO ENTRE 0 E 10. SÓ QUE AGORA O JOGADOR VAI
TENTAR ADVINHAR ATÉ ACERTAR, MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.
"""
from random import randint

computador = randint(0,10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. Qual é seu palpite?')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. Qual é seu palpite?')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))


