"""
ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO => 'WHILE'
# EXEMPLO01
for c in range(1, 10):
    print(c)
print('FIM')
#EXEMPLO02
c = 1 #=> C COMEÇA COM 1
while c < 10: #=> ENQUANTO C FOR MENOR QUE 10
    print(c) #=> MOSTRAR C
    c = c + 1 #=> C RECEBE C + 1
print('FIM')
#EXEMPLO03
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('FIM')
"""
#EXEMPLOS
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

