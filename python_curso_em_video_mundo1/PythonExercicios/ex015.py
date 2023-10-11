# Escreva um programa que converta uma temperatura digitada em C° e converta para °F.

c = float(input('Insira a temperatura C°:'))
f = ((9 * c) / 5) + 32
print('-' * 48)
print('A temperatura de {}C° corresponde a {}°F!'.format(c, f))
print('-' * 48)

