"""
ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO.
SE ELE ULTRAPASSAR 80KM/H, MOSTRE UMA MENSAGEM DIZENDO QUE ELE FOI MULTADO.
A MULTA VAI CUSTAR R$7,00 POR CADA KM ACIMA DO LIMITE.

"""


v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    multa = (v - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
print('---------------FIM---------------')



