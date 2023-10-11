"""
DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. NO FINAL DEO PROGRAMA, MOSTRE:
A MÉDIA DE IDADE DO GRUPO.
QUAL O NOME DO H0MEM MAIS VELHO.
QUANTAS MULHERES TÊM MENOS DE 20 ANOS.
"""

somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomemaisvelho = ''
totmulher = 0
for pess in range(1, 5):
    print('---- {}° PESSOA -----'.format(pess))
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('[M/F]: ')).strip()
    somaidade = somaidade + idade
    if pess == 1 and sexo in 'Mn':
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomemaisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher = totmulher + 1
    mediaidade = somaidade / pess
print('A média de idade do grupo foi de {} anos'.format(mediaidade))
print('O home mais velho tem {} e se chama {}'.format(maioridadehomem, nomemaisvelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totmulher))
