"""
FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. NO FIANL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.
"""
maior = 0
menor = 0
for pess in range(1, 6):
    peso = int(input('Peso da {}° pessoa: '.format(pess)))
    if pess == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O menor peso lido foi de {}Kg'.format(menor))
