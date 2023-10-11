"""
FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER EM MOSTRE O SEU FATORIAL;
EX:
5!=5X4X3X2X1=120

#>> EXEMPLO USANDO MÓDULO
from math import factorial 
valor = int(input('Digite um número para calcular seu Fatorial: '))
f= factorial(valor)
print("""#Calculando {}!
#O fatorial de {} é {}.
""" .format(valor, valor, f) )

#>> EXEMPLO SEM USAR MÓDULO
valor = int(input('Digite um número para calcular seu Fatorial: '))
c = valor #>> contador do número digitado
f = 1 # >> todo número multiplicado por 1 é = ele mesmo. O limite aqui é até 1
print('Calculando {}! = '.format(valor), end='')
while c > 0: #>> enquanto o contador for maior que zero
  print('{}'.format(c), end='')# >> "end=''" evita que ele pule linha
  print('x' if c > 1 else ' = ', end='')
  f *= c #>> fatorial multiplicando contagem 
  c -= 1 #>> regressiva até 1
print('{}'.format(f)) #>> fora do laço de 'while'
"""
