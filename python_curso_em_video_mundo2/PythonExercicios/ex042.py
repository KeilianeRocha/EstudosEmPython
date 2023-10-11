"""
A CONFEDERAÇÃO DE NATAÇÃO PRECISA DE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
- ATÉ 9 ANOS: MIRIM
- ATÉ 14 ANOS: INFANTIL
- ATÉ 19 ANOS: JUNIOR
- ATÉ 25 ANOS: SÊNIOR
- ACIMA: MASTER

"""
from datetime import date

nasc = int(input('Ano de Nascimento: '))
idade = date.today().year - nasc
if idade <= 9:
    print('O atleta tem {} anos \nClassificação: MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos \nClassificação: INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos \nClassificação: JUNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos \nClassificação: SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos \nClassificação: MASTER'.format(idade))
