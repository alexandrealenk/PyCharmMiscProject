nome = 'Alexandre'
cores = {'limpa':'\033[m',
         'azul':'\33[34m',
         'amarelo':'\33[33m',
         'pretoebranco': '\33[7:30m'}
print('Olá, muito prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
