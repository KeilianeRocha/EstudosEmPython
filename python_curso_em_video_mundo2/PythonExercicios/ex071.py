"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a
ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
print('='*51)
print('-'*20, '\033[1;34mBANCO DEV\033[m', '-'*20)
print('='*51)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
ced = 100
totalCed = 0
while True:
    if total >= ced: #> total menor = ced
        total -= ced #> total debita da ced
        totalCed += 1 #> total ced + 1
    else:
        if totalCed > 0:
            print(f'Total de {totalCed} cédulas de R${ced:.2f}')
        if ced == 100:#> ced for igual a 50
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalCed = 0
        if total == 0:
            break
print('='*50)
print('-' * 11, '\033[1;34mVolte sempre ao BANCO DEV!\033[m', '-' * 11)
print('='*50)

