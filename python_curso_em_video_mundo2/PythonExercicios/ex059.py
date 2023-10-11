"""
CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:
[1] SOMAR
[2] MULTIPLICAR
[3] MAIOR
[4] NOVOS NÚMEROS
[5] SAIR DO PROGRAMA
SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.
"""
from time import sleep

valor1 = int(input('Primeiro valor: '))
valor2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
  print("""
  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos números
  [5] Sair do programa 
  """)
  opcao = int(input('Qual é a sua opção? ' ))
  if opcao == 1:
    soma = valor1 + valor2
    print('A soma de {} + {} é {}'.format(valor1, valor2, soma)),
  elif opcao == 2:
    multiplica = valor1 * valor2
    print('A multiplicação de {} x {} é {}'.format(valor1, valor2, multiplica))
  elif opcao == 3:
    if valor1 > valor2:
      maior = valor1
    else:
      maior = valor2
    print('O maior valor digitado foi {}'.format(maior))
  elif opcao == 4:
    print('Digite novos valores')
    valor1 = int(input('Primeiro valor: '))
    valor2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Fim do programa!')
  else:
    print('Opção inválida!')
    print('=-=' *10)
    sleep
