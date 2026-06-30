from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=' * 30)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=' * 30)
jogador = int(input('Em que número eu pensei? ')) #jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}.'.format(computador, jogador))
