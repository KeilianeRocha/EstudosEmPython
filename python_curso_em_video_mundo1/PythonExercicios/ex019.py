# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O Ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O Ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, coseno))
print('O Ângulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))