# Faça um algoritmo que leia p preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Insira o valor do produto R$'))
print('-'*24)
print(f'Preço Bruto R$:{produto:.2f}')
desconto = produto - (produto * 5 / 100)
print('Com o Desconto de 5%\nO Valor Total é R$:{:.2f}'.format(desconto))
print('-'*24)
