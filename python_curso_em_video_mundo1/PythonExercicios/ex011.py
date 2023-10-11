# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considere: USS 1.00 = 3. 27

carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 3.27
print(f'Com R${carteira:.2f}\nVocê pode comprar {dolar:.2f} Dólares')
