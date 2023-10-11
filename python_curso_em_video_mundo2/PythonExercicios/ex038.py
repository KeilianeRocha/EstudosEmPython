"""
ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO:
- PARA BINÁRIO
-2 PARA OCTAL
-3 PARE HEXADECIMAL

"""
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO 
[ 2 ] Converter para OCTAL 
[ 3 ] Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}{}{}'.format(n, '\033[0;32m', bin(n)[2:], '\033[m'))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}{}{}'.format(n, '\033[0;34m', oct(n)[:2], '\033[m'))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}{}{}'.format(n, '\033[0;33m', hex(n)[:2], '\033[m'))
else:
    print('Opção \033[0;31minválida!\033[m Tente novamente')
