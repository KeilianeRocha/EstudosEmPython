# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

"""from math import trunc

num = float(input('Digite um número: '))
print('O valor número digitado foi: {} e a sua porção inteira é: {}'.format(num, trunc(num)))
=> usando a importação de uma funcionalidade do módulo 'math'
"""

num = float(input('Digite um número: '))
print('O valor número digitado foi: {} e a sua porção inteira é: {}'.format(num, int(num)))
# => Sem inportar módulos ou funcionalidades.
