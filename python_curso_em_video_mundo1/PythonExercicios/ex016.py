# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 POR km.

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km percorridos? '))
pago = (dias * 60) + (km * 0.15)
print('-' * 38)
print('Dias alugado:{:2}\nDistância percorrida {}Km\nTotal a pagar R$:{:.2f}'.format(dias,km, pago))
print('-' * 38)

