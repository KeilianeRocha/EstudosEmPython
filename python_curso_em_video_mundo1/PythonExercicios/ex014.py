# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Insira o valor do salário do funcionário R$'))
aumento = salario + (salario * 15 / 100)
print('-'*48)
print(f'Salário Bruto R$:{salario:.2f}')
print('Com 15% de aumento\nO valor Total do Salário é R${:.2f}'.format(aumento))
print('-'*48)

