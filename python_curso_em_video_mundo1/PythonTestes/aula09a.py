# MANIPULANDO TEXTO
# FATIAMENTO STRING

# FRASE = [C][U][R][S][O] [E][M] [V][I][D][E][O]
#          0  1  2  3  4 5 6  7 8 9 10 11 12 13

# FATIAMENTO DE STRING => FRASE[9] => [V]9 => ÍNDICE DENTRO DA STRING
# FATIAMENTO DE STRING => FRASE[9:13] => [V][I][D][E]9 10 11 12 => SEMPRE UM AMENOS NO FINAL
# FATIAMENTO DE STRING => FRASE[9:14] => [V][I][D][E][O]9 10 11 12 13
# FATIAMENTO DE STRING => FRASE[9:14:2] => [V][D][O]9 11 13 => VAI SALTANDO DE 2 EM 2
# FATIAMENTO DE STRING => FRASE[:5][C][U][R][S][O]0  1  2  3  4 5 => COMO NÃO INFORMEI O INICIU, ELE COMEÇA DO '0'
# FATIAMENTO DE STRING => FRASE[9:] => [V][I][D][E][O] 9 10 11 12 13 => COMO NÃO INFORMEI O FINAL, ELE PEGOU TODA A
# FRASE
# FATIAMENTO DE STRING => FRASE[9::3] => [V][E]9 12 => COMO NÃO INFORMEI O FINAL, ELE PEGOU TODA A FRASE E
# PULOU DE 3 EM 3

# ANÁLISE STRING
# FRASE = [C][U][R][S][O] [E][M] [V][I][D][E][O] LETRAS E MICRO ESPAÇOS
#          0  1  2  3  4 5 6  7 8 9 10 11 12 13

# LEN(FRASE) => O CUMPRIMENTO OU MICROESPAÇOS
# FRASE.COUNT('O') => QUANTAS VEZES 'O' APARECE NA FRASE OU
# FRASE.COUNT('O', 0, 14) => CONTA DO INICIO AO FINAL DA FRASE , QUANTOS 'O' TEM
# FRASE.FIND('DEO') => MOSTRA EM QUE MOMENTO COMEÇOU O 'DEO'
# FRASE.FIND('TEXTO') => QUANDO EU COLOCO UM VALOR QUE NÃO EXISTE, ELE RETONAR -1
# 'CURSO'IN FRASE => PERGUNTA SE DENTRO DA STRING EXISTE O VALOR 'CURSO' RETORNA TRUE

#TRANSFORMAÇÃO STRING
# => POR MEIO DE MÉTODOS
# FRASE = [C][U][R][S][O] [E][M] [V][I][D][E][O] LETRAS E MICRO ESPAÇOS
#          0  1  2  3  4 5 6  7 8 9 10 11 12 13

# FRASE.REPLACE('VIDEO', 'ANDROID') => ELE VAI PROCURAR 'VIDEO' E TROCA POR 'ANDROID'
# FRASE.UPPER() => TRANFORMA A STRING PARA CAIXA ALTA
# FRASE.LOWER() => TRANSFORMA A STRING PARA MINÚSCULO
# FRASE.CAPITALIZE() => TRANSFORMA TODOS PARA MINÚSCULO E A 1° MAIÚSCULA
# FRASE.TITLE() => ANALISA QUANTAS PALAVRAS TEM A FRASE E TRASFORMA AS QUEBRAS COM A 1° MAIÚSCULA
# FRASE.STRIP() => REMOVE ESPAÇOS SEM USO DA STRING
# FRASE.RSTRIP() => REMOVE SOMENTE OS ESPAÇOS DA DIREITA MANTEM OS DA ESQUERDA
# FRASE.LSTRIP() => REMOVE OS ESPAÇOS DA ESQUERDA E MANTEM OS DA DIREITA

#DIVISÃO STRING
# => VAI OCORRER UMA DIVISÃO DENTRO DA STRING, CONSIDERANDO OS ESPAÇOS SEM USO
# FRASE = [C][U][R][S][O][E][M][V][I][D][E][O] LETRAS E MICRO ESPAÇOS
#          0  1  2  3  4  0  1  0  1  2  3  4
#                0          1          2

# FRASE.SPLIT() => DIVIDE UMA STRING EM UMA LISTA, CADA ELEMENTO VAI SER SEPARADO PELO SEU SPLITADOR (ESPAÇO)

#JUNÇÃO STRING
# => VAI OCORRER A JUNÇÃO DAS LISTAS
# FRASE = [C][U][R][S][O][E][M][V][I][D][E][O] LETRAS E MICRO ESPAÇOS
#          0  1  2  3  4  0  1  0  1  2  3  4
#                0          1          2

# '-'.JOIN(FRASE) => VAI JUNTAR AS LISTA E COLOCAR UM '-' ENTRE ELAS => CURSO-EM-VIDEO
frase = 'Curso em Vídeo Python'
frase = frase.replace('Python', 'Android')
print(frase)
print(frase[3:13])
print(frase[:13])
print(frase[1:15:2])
print(frase[::2])
print(frase[3])
texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vitae auctor neque. Phasellus ultrices neque
nibh, sit amet vulputate sapien accumsan nec. Vivamus fringilla libero id odio dictum, ac sagittis mi congue. Nulla 
consequat suscipit orci ac gravida. Cras porttitor lorem eu metus congue rhoncus. Phasellus id ligula condimentum, 
commodo nisl nec, sodales ligula. Morbi auctor aliquet enim sed sagittis. Aenean a sagittis metus, ultrices convallis 
nisl. Nunc a erat cursus, vestibulum ligula vitae, aliquam nulla. Aenean lobortis consequat fringilla. Ut ornare viverra
diam, in egestas dolor feugiat ac. Duis eget nisi porttitor, egestas orci a, sagittis eros. Ut a massa eu dolor placerat
laoreet. Mauris accumsan vitae magna vitae rutrum. Curabitur ut commodo tortor."""

print(texto.count('o'))
print('gravida' in texto)
print(texto.find('gravida'))
print(texto.split())




