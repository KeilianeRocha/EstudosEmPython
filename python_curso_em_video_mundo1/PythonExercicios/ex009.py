#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros.

medida = float(input('Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
print(f'A medida de {medida:.0f}m corresponde a {cm:.0f}cm e {mm:.0f}mm')

