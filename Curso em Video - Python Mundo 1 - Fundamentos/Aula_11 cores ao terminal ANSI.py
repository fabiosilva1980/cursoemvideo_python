# Primeiros passos de cores no terminal

# Nessa aula, vamos aprender como utilizar os códigos de escape sequence ANSI para
# configurar cores para os seus programas em Python.
# Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# Utilizamos o padrão ANSI - escape sequence
# O codigo ansi funciona melhor com o padrão 033 (\033)
# O codigo ansi segue o padrão abaixo:
#   \033[STYLE;TEXT;BACKm
#   STYLE -> comportamento, estilo do texto (normal, sublinhado, negrito
#   TEXT -> cor do texto
#   BACK -> cor de fundo do texto

# Código para Style
#   = 0 (normal),
#   = 1 (Negrito - Bold),
#   = 4 (sublinhado - Underline),
#   = 7 (Inverte as cores - Negative)
# -> codigos que funcionam melhor no python

# Código de cores para TEXT e BACK
#  Cod.TEXT  Cod.BACK
#   -> 30       40   - White
#   -> 31       41   - Red
#   -> 32       42   - Green
#   -> 33       43   - Yellow
#   -> 34       44   - Blue
#   -> 35       45   - Magenta
#   -> 36       46   - Ciano
#   -> 37       47   - Grey

# OBSERVAÇÃO: para finalizar a inserção de cores em um texto adicionar ao final da frase \033[m,
#             onde finaliza a seleção e volta o texto a cor padrão do terminal

# exemplo: print('\033[0;33;44mTEXTO_XPTO\033[m')

# Exemplos na prática
print('\033[0;30;41mTeste\033[m') #     Texto normal; Letra branca; fundo vermelho
print('\033[4;33;44mTeste1\033[m') #    Texto sublinhado; Letra Amarela; fundo Azul
print('\033[1;35;43mTeste2\033[m') #    Texto negrito; letra Magenta; fundo Amarelo
print('\033[30;42mTeste3\033[m') #      Texto normal; letra Branca; fundo verde
print('\033[7;30mTeste4\033[m') #       Texto Negativo; letra Branca - qdo invertido a cor da letra passa a ser de fundo

print('\033[1;31;44mOlá, Mundo!\033[m')
print('\033[7;30;44mOlá, Mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[1;33m{}\033[m'.format(a, b))

# alterando cores no .format()
nome = 'Fabio'
print('Olá! Muito prazer em te conhecer {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

# Em forma de dicionário:
cores = {
    'limpa':'\033[m',
    'azul':'\033[34m',
    'amarelo':'\033[33m',
    'pretoebranco':'\033[7;30m'
}
print('Não sei qual cor escolher {}{}{}!?!?'.format(cores['amarelo'], nome, cores['limpa']))
