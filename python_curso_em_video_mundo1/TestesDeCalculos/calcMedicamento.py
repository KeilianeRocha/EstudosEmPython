idade = int(input('Insira a idade do paciente: '))
peso = int(input('Insira o peso do paciente: '))

dosagem = 0

if (idade  >= 12 and peso >= 60):
    dosagem = 1000
elif (idade >=12 and peso < 60):
    dosagem = 875
else:
    dosagem = peso *2

quantidadedeGotas = dosagem / 500 * 20

print('A dosagem do medicamento é ', dosagem, ' mg.')
print('O paciente deve tomar ', quantidadedeGotas, ' gotas por dose.')