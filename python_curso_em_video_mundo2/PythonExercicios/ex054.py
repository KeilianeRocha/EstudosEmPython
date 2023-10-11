"""
FAÇA UM PROGRMA QUE LEIA UMA FRASE QUALQUER E DIGA SE ELA É UM 'PALÍNDROMO', DESCONSIDERANDO OS ESPAÇOS.
EX:
APOS A SOPA
A SACADA DA CASA
A TORRE DA TERROTA
O LOBO AMA O BOLO
"""
plvr = str(input('Digite uma palavra: ')).strip().upper()
plvr = plvr.split()
junto = ''.join(plvr)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso da frase {} é {}'.format(junto, inverso))
if inverso == junto:
    print('É PALÍNDROMO')
else:
    print('A frase difgitada Não é PALÍNDROMO')
