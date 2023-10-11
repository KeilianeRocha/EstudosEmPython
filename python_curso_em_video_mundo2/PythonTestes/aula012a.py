nome = str(input('Qual é seu nome? ')).title().strip()
if nome == 'Keila':
    print('Que nome lindo!')
elif nome == 'Karla' or nome == 'Maria' or nome == 'Juliana':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Jaqueline Patrícia Mara':
    print('Belo nome feminino! ')
else: #=> É OPCIONAL
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

