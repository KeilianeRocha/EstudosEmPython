"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar
ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
"""
tot = 0
tot1000 = 0
menor = 0
cont = 0
barato = 0
print('-'*10, '\033[1;34mMERCADO TECH\033[m', '-'*10)
while True:
    prdNome = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço: R$'))
    tot += preco
    cont += 1
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if preco >= 1000:
        tot1000 += 1
    if cont == 1 or preco < menor: #>> forma mais resumida
        menor = preco
        barato = prdNome
    """else:
        if preco < menor:
            menor = preco
            barato = prdNome""" #>> segunda forma
    if opcao == 'N':
        print(f"""O total da compra foi R${tot:.2f}
Temos {tot1000} produtos custando mais de R$1000.00
O produto mais barato foi {barato} que custa R${menor:.2f}""")
        break
print('-' * 10, '\033[1;31mFIM DO PROGRAMA\033[m', '-' * 10)
