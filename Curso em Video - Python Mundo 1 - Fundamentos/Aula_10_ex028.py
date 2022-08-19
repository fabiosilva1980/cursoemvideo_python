# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual o número escolhido pelo computador.
# o Programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
num = randint(0,6)
print('---' * 20)
print('Vou pensar em um número de 0 a 5, tente adivinhar ...')
print('---' * 20)
user = int(input('Adivinhe em que número estou pensando? \n Digite um número de 0 a 5: '))
print('PROCESSANDO...')
sleep(3)
if user == num:
    print('VOCÊ ACERTOU PARABÉNS !!! \n Eu escolhi o número {}'.format(num))
else:
    print('Você Errou :( \n O número que escolhi foi {}\n Tente outra vez!'.format(num))
