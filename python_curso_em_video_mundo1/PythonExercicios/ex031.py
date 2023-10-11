"""
DESENVOLVA UM PROGRAMA QUE PERGUNTA A DISTÂNCIA DE UMA VIAGEM EM KM.
CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA VIAGENS DE ATÉ 200 KM E R$0,45 PARA VIAGENS MAIS LONGAS.

"""
distancia = float(input('Qual a distância da sua viagem? '))
if distancia <= 200:
    preco = distancia * 0.50
    print('Você está restes a começar uma viagem de {}Km'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))
else:
    preco = distancia * 0.45
    print('Você está restes a começar uma viagem de {}Km'.format(distancia))
    print('E o preço da sua passagem será de R${:.2f}'.format(preco))