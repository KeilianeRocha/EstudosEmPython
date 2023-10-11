# Crie um algoritmo que leia um n[umero e mostre o seu dobro, triplo e a raiz quadrada.

numero = int(input('Insira um valor '))
# print(f"O dobro de {numero} é {numero * 2}\nE o triplo é {numero * 3}\ne a raiz quadrada é {numero ** (1 / 2):.2f}")
# OUTRA FORMA
print(f"O dobro de {numero} é {numero * 2}\nE o triplo é {numero * 3}\ne a raiz quadrada é {pow(numero, (1 / 2)):.2f}")
# => USANDO A FUNÇÃO 'POW'.
