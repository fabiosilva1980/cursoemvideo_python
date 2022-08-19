# Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e
# from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos
# adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

# Por exemplo para importar uma biblioteca utilizamos o comando IMPORT Biblioteca
# Se queremos uma funcionalidade especifica dessa biblioteca utilizamos FROM Biblioteca IMPORT Funcionalidade.
# Este metodo economiza memoria trazendo apenas a função necessário oara a execução do script.

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é {}.'.format(num,raiz))
# ou podemos utilizar a funcionalidade math.ceil(raiz) para arredondar para mais ou
# math.floor(raiz) para arredondar para menos

from math import sqrt # para lista a funcionalidade de uma biblioteca CTRL + espaço
raiz = sqrt(num) # não precisa colocar a biblioteca
print('A raiz quadrada de {} é {}.'.format(num,raiz))

import random
num = random.random()
print(num)

import emoji
print(emoji.emojize('Olá Mundo :sunglasses: :earth_americas:', use_aliases=True))
