# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math # importando a biblioteca
num = float(input('Digite um valor: ')) # pode ser a função FLOOR ou TRUNC neste caso
inteiro = math.floor(num)
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num,inteiro))

from math import floor # importando somente o modulo de uma biblioteca
print('O valor digitado foi {} e a sua porção inteira é {}.'.format(num, floor(num)))

print('O valor digitado foe {} e a sua porção inteira é {}.'.format(num,int(num))) # utilizando uma função interna do python (INT)
