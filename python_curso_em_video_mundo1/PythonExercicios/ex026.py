# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME.

nome = str(input('Qual o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('Silva' in nome.title()))
