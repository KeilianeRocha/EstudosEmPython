"""
CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A
MÉDIA ATINGIDA:
- MÉDIA ABAIXO DE 5.0: REPROVADO
- MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
- MÉDIA 7.0 OU SUPERIOR: APROVADO

"""
print('\033[44m BOLETIM ESCOLAR \033[m')
nota1 = float(input('1° nota: '))
nota2 = float(input('2° nota: '))
nota3 = float(input('3° nota: '))
nota4 = float(input('4° nota: '))
media = (nota1 + nota2 + nota3 + nota4) / 4
print('''\033[34m RESULTADO FINAL: \033[m
Nota 1° - {}
Nota 2° - {}
Nota 3° - {}
Nota 4° - {}\nSua média foi {}{}{}.'''
      .format(nota1, nota2, nota3, nota4, '\033[1m', media, '\033[m'))

if 7 > media >= 5:
    print('Aluno está de \033[33mRECUPERAÇÃO!\033[m')
elif media < 5:
    print('Aluno está \033[31mREPROVADO!\033[m')
else:
    print('Aluno está \033[32mAPROVADO!\033[m')

