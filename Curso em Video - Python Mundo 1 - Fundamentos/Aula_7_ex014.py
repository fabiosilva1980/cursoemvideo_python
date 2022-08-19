# Escreva um programa que converta uma temperatura digitando em graus Celsius e
# converta para graus Fahrenheit

c = float(input('Informe a temperatura em ºC: '))
f = 1.8 * c + 32
print('A temperatura em Celsius {:.1f}ºC, em Fahrenheit é {:.1f}ºF'.format(c,f))
print('{:.1f}'.format((f - 32) / 1.8))
