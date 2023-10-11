# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

objeto = input('Digite algo: ')

print(f'O tipo primitivo desse valor é: ', type(objeto))
print('Só tem espaços? ', objeto.isspace())
print('É um número? ', objeto.isnumeric())
print('É alfabetico? ', objeto.isalpha())
print('É alfanumérico? ', objeto.isalnum())
print('Está em maiúsculas? ', objeto.isupper())
print('Está em minúsculas? ', objeto.islower())
print('Está capitalizada? ', objeto.istitle())