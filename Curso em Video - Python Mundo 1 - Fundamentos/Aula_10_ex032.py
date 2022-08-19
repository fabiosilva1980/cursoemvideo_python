# Faça um programa que leia um ano qualquer e mostre se o ano é BISSEXTO.
ano = int(input('Qual o ano que será analisado, caso seja o ano atual digite 0: '))

# O ano bissexto ele pode ser dividido por 4 não pode ser divisivel por 100 e algumas vezes pode ser divisivel por 400
# Anos que não são bissextos por exemplo para divisiveis por 400 - 1700 e 1900
# a = ano % 4
# b = ano % 100
# c = ano % 400
# Condição de bissexto -> a == 0 and b != 0 or c ==0

from datetime import date # para importar o modulo de data simples
if ano == 0:
    ano = date.today().year # para demostrar apenas o ano atual
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é um ano BISSEXTO.".format(ano))
else:
    print('Este ano de {} não é um ano BISSEXTO.'.format(ano))
