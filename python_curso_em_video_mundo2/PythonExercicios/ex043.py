"""
REFAÇA O DESAFIO 035 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE MOSTRA QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
- EQUILÁTERO: TODOS OS LADOS IGUAIS
- ISÓSCELES: DOIS LADOS IGUAIS
- ESCALENO: TODOS OS LADOS DIFERENTES

"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os seguimentos acima PODEM FORMAR triângulo', end=' ')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os seguimentos acima  NÃO PODEM FORMAR triângulo!')