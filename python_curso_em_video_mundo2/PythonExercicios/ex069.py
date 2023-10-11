"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se
o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
totm = totf = 0
tot18 = tot20 = 0

while True:
    print('-'*25)
    print('CADASTRE UMA PESSOA')
    print('-'*25)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MnFf':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    print('Cadastro realizado com sucesso!')
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totm += 1
    if idade <= 20:
    # if idade <= 20 and sexo == 'F' >> outra forma de escrever o cód.
        if sexo == 'F':
            totf += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    # print('Dados inválidos!')
    if resp == 'N':
        print('Fim.')
        break
print(f"""Total PESSOAS com MAIS de 18 anos: \033[1;4;34m{tot18}\033[m.
Ao todo temos \033[1;34m{totm} HOMENS\033[m cadastrados e,
\033[1;35m{totf} MULHERES\033[m com MENOS de 20 anos""")
















