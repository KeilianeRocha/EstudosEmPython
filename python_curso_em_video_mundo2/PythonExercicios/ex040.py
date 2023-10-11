"""
FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM E INFORME, DE ACORDO COM SUA IDADE:
- SE LE IANDA VAI SE ALISTAR AO SERVIÇO MILITAR.
- SE É A HORA DE SE ALISTAR.
- SE JÁ PASSOU DO TEMPO DO ALISTAMENTO.
SEU PROGRMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

"""
from datetime import date

nasc = int(input('Ano de aniversário: '))
atual = date.today().year
idade = date.today().year - nasc

print('''Quem nasceu em {}{}{} tem {}{}{} anos em {}{}{}'''
      .format('\033[4m', nasc, '\033[m', '\033[0;32m', idade, '\033[m', '\033[1m', atual, '\033[m'))
if idade == 18:
    print('Você tem que se alistar \033[0;31mIMEDIATAMENTE!\033[m')
elif idade < 18:
    alistamento = 18 - idade
    print('Ainda faltam {} anos para seu alistamento.'.format(alistamento))
    saldo = atual + alistamento
    print('Seu alistamento será em {}{}.{}'.format('\033[0;42m', saldo, '\033[m'))
else:
    alistamento = idade - 18
    print('Você deveria ter se alistado há {}{} anos{}.'.format('\033[0;31m', alistamento, '\033[m'))
    saldo = atual - alistamento
    print('Seu alistamento foi em {}{}.{}'.format('\033[41m', saldo, '\033[m'))




