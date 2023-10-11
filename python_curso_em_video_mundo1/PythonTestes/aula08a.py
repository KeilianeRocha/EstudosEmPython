import  emoji
"""
MÓDULOS
COMANDO PARA IMPORTAR TUDO, PRIMEIRA LINHAS => IMPORT EXEMPLO
COMANDO PARA IMPORTAÇÃO ÚNICA => FROM EXEMPLO IMPORT EXEMPLO
EXEMPLO DE BIBLIOTECA:> MATH

"""
import math  # => importei um módulo 'math'
from math import sqrt  # => importer somente uma funcionalidade do módulo 'math'

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz))) #=> comando 'math.ceil' usado para aredondar o
# resultado para cima.
print('A raiz de {} é igual a {}'.format(num, math.floor(raiz)))  # => comando 'math.ceil' usado para aredondar o
# resultado para baixo.
