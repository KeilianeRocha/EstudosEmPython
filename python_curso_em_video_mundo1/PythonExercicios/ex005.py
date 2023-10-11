"""nome = input('Qual é o seu nome? ').capitalize()
print(f'\nPrazer em te conhecer {nome:^20}') #=> centraliza """

n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
print(f'A soma é {s}\nO produto é {m}\nE a divisão é {d:.3f}', end=' ') #=> une os prints em 1 linha
print(f'\nA divisão inteira é {d:.3f}\nE a potência  é {p:.3f}')