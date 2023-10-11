"""
CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A
 MAIORIDADE Q QUANTAS JÁ SÃO MAIORES.
"""
from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? :'.format(pess)))
    idade = date.today().year - ano
    #print(idade)
    if idade >= 21:
        totmaior += 1
        #print('Essa pessoa e Maior')
    else:
        totmenor += 1
        #print('Essa pessoa é Menor')
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('Ao todo tivemos {} pessoas menores de idade'.format(totmenor))

