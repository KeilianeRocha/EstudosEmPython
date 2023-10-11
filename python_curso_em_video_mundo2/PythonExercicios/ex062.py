"""
MELHORE O DESAFIO 062, PERGUNTANDO PARA O USUÁRIO SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. O PROGRAMA ENCERRA QUANDO ELE
 DISSER QUE QUER MOSTRAR 0 TERMOS.
"""
print('Gerador de PA')
primeiro = int(input('Primeiro Termo '))
razao = int(input('Razão '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} => '.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos'.format(total))
print('Fim')