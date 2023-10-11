"""
ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE
PAGAMENTO:
- À VISTA DINHEIRO/ CHEQUE: 10% DE DESCONTO
- À VISTA NO CARTÃO:5% DE DESCONTO
- EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
- 3X OU MAIS NO CARTÃO: 20% DE JUROS

"""
print('{:=^40}'.format('LOJA MILY')) # => formatação para centralizar a mensagem
produto = float(input('Preço da compra: R$ '))
calc = produto - (produto * 10/100)
print(calc)

print('''Formas de apagamento
[ 1 ] - À vista DINHEIRO/CHEQUE
[ 2 ] - À vista no CARTÃO
[ 3 ] - Em ate 2X no CARTÃO
[ 4 ] - 3X ou mais no CARTÃO''')
opcao = int(input('Opção: '))
if opcao == 1:
    calc = produto - (produto * 10 / 100)
    print('Valor Bruto: R${:.2f}'.format(produto))
    print('Valor Total com 10% de Desconto: R${:.2f}'.format(calc))
elif opcao == 2:
    calc = produto - (produto * 5 / 100)
    print('Valor Bruto: R${:.2f}'.format(produto))
    print('Valor Total com 5% de Desconto: R${:.2f}'.format(calc))
elif opcao == 3:
    print('Valor Bruto: R${:.2f}'.format(produto))
    print('Valor Total: R${:.2f}'.format(produto))
else:
    calc = produto + (produto * 20 / 100)
    print('Valor Bruto: R${:.2f}'.format(produto))
    print('Valor Total com 20% de Juros: R${:.2f}'.format(calc))
print(print('{:=^40}'.format('Volte Sempre!'))) # => formatação para centralizar a mensagem
