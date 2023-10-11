# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.

nome = str(input('Digite seu nome completo: ')).strip().title()
n = nome.split()
print(nome)
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {} '.format(n[0]))
print('Seu último nome é : {} '.format(n[len(n)-1]))



