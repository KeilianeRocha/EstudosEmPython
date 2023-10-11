"""
CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR
999, QUE É A CONDIÇÃO DE PARADA. NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS E QUAL FOI A SOMA ENTRE ELES
(DESCONSIDERANDO O FLAG).
"""

cont = 0
soma = 0
num = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1 #> aqui impede que o flag seja contado.
print(f'Você digitou {cont} números e a soma entre eles é {soma}.')
print('Fim')