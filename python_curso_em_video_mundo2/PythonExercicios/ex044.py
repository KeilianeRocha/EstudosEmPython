"""
DESENVOLVA UMA LÓGICA QUE LEIA O PESO E ALTURA DE UMA PESSOA, CALCULE SEU IMC E MOSTRE SEU STATUS, DE ACORDO COM A
TEBELA ABAIXO:
- ABAIXO DE 18.5: ABAIXO DO PESO
- ENTRE 18.5 E 25: PESO IDEAL
- 25 ATÉ 30: SOBREPESO
- 30 ATÉ 40: OBESIDADE
- ACIMA DE 40: OBESIDADE MÓRBIDA

"""
peso = float(input('Qual o seu peso? (Kg) '))
altura = float(input('Qual a sua altura? (Cm) '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é de {:.1F}'.format(imc))
if imc < 18.5:
    print('Você esta ABAIXO do peso')
elif imc >= 18.5 and imc < 25:
    print('Você esta com o PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você esta com SOBREPESO!')
elif imc >= 30 and imc < 40:
    print('Você esta com OBESIDADE!')
else:
    print('Você esta com OBESIDADE MÓBIDA!')