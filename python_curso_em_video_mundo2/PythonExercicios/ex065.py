"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a
digitar valores.
"""

cont = 0
media = 0
soma = 0
maior = 0
menor = 0
resp = 's'
while resp in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = (input('Quer continuar? [S/N] ')).strip().lower()
    while True:
        if resp in ['s', 'n']:
            break
        else:
            resp = input('Opção inválida! Quer continuar? [S/N]').strip().lower()
if cont > 0: #>> verificação para evitar que haja divisão por 0.
    media = soma / cont
print("""Você digitou {} números  e a média foi {:.2f}
O maior valor foi {} e o menor foi {}""".format(cont, media, maior, menor))
print('Fim!')








