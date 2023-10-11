# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:

# => O NOME COM TODAS AS LETRAS MAIÚSCULAS
# => O NOME COM TODAS AS LETRA MINÚSCULAS
# => QUANTAS LETRAS AO TODO (SEM CONSIDERAR ESPAÇOS).
# => QUANTAS LETRAS TEM O PRIMEIRO NOME.

nome = str(input('Digite um nome: ')).strip()
print('Analisando seu nome...')
# print(nome.title().split())
print('Seu nome me maiúsculas é: {}'.format(nome.upper()))
print('Seu nome me minúsculas é: {}'.format(nome.lower()))
print('Seu nome ao total tem {} letras'.format(len(nome)-nome.count(' ')))
print('Seu primeiro tem {} letras'.format(nome.find(' ')))
