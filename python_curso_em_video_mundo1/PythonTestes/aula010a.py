# ESTRUTUTAS CONDICIONAIS
"""
# => CONDIÇOES SIMPLES
# tempo = int(input('Quantos anos tem seu carro? '))
# print('Carro NOVO'if tempo <= 3 else'Carro VELHO')
# print('--FIM--')
# ----------------------------------------------------------------------------------------------------------------------

# => CONDIÇOES COMPOSTAS

nome = str(input('Qaual é o seu nome? ')).strip().title()
if nome == 'Keila':
    print('Que nome lindo {}!'.format(nome))
else:
    print('Bom dia {}!'.format(nome))
print('-------------FIM-------------')
# ----------------------------------------------------------------------------------------------------------------------

# => ESTRUTURA SEQUENCIAL
# => ESTRUTURA DE INDENTAÇÃO
# ----------------------------------------------------------------------------------------------------------------------

EM UMA ESTRUTURA DE CONDIÇÃO OU O BLOCO 'TRUE' VAI SER EXECUTADO, OU O BLOCO 'FALSE', NUNCA OS DOIS.
EXEMPLO =>  if carro.esquerda():
                bloco True => com T maiúsculo
           else:
                bloco False => com F maiúsculo
# ----------------------------------------------------------------------------------------------------------------------
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro NOVO')
else:
    print('Carro VELHO')
print('--FIM--')                

"""

n1 = float(input('Digite a Primeira nota: '))
n2 = float(input('Digite a Segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m <= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média não foi boa! ESTUDE MAIS!')
print('-------------FIM-------------')


