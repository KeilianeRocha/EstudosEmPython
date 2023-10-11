#Crie um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Insira o valor da nota 1: '))
nota2 = float(input('Insira o valor da nota 2: '))
s = nota1 + nota2
print(f'A soma da NOTA1 e NOTA2 é: {s:.2f}\nE a média das duas notas é: {s/2:.2f}')
