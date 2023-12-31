"""
Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando
 o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    opcao = ' '
    while opcao not in 'PpIi':
        opcao = str(input('Par ou Ímpar [P/I]? ')).strip().upper()[0] #> pesquisar a diferença de 'upper e lower'
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('Deu PAR' if total %2 ==0 else 'Deu ÍMPAR')
    if opcao == 'P':
        if total % 2 == 0:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    elif opcao == 'I':
        if total % 2 == 1:
            print('Você GANHOU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print(f'Game over! Você venceu {v} vezes.')






