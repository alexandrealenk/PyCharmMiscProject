nome = str(input('Digite seu nome completo: ')).strip() #Remover espaços em braco
print('Analisando seu nome...')
print('Seu nome em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome minúsculo é: {}'.format(nome.lower()))
print('Tem o total de {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() #quebra a string em pedaços
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0], len(separa[0])))
