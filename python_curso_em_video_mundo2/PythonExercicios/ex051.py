"""
DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. SE O VALOR
DIGITADO FOR IMPAR, DESCONIDERAR.
"""

soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input('Digite o {}° valor '.format(c)))
    if numero % 2 == 0:
        soma += numero
        cont += 1
      # soma = soma + 1
print('A soma dos valores {} é igual a {}'.format(cont, soma))
