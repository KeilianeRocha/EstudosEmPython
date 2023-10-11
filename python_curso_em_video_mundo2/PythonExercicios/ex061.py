"""
REFAÇA O DESAFIO 052, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO
A ESTRUTURA WHILE
"""
print('Gerador de PA')
primeiro = int(input('Primeiro Termo '))
razao = int(input('Razão '))
termo = primeiro
cont = 1
while cont <= 10:
  print('{} => '.format(termo),end='')
  termo += razao
  cont += 1
print('Fim')