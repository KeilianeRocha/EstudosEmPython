"""
ANSI => escape sequence
\035[codDaCorm

"""
print('\033[1;34mOlá, mundo!\033[m')
nome = 'Keiliane'
print('meu nome é {}{}{}'.format('\033[4;34m', nome, '\033[m'))

print('\033[1;35mOlá, mundo!\033[m')
print('\033[1;4;37mOlá, mundo!\033[m')