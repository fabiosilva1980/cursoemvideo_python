# Faça um programa que leia o comprimimento do cateto oposto e do cateto adjacente de um triangulo retangulo.
# Calcule e  mostre o comprimento da hipotenusa

from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
# hp = (co ** 2 + ca ** 2) ** (1/2) # soma dos quadrados e dos catetos é igual a raiz quadrada da hipotenusa
hp = hypot(co,ca) # import biblioteca
print('O triangulo retângulo possuí um dos ângulos de 90º, seu cateto oposto é de {} possuí o cateto adjacente é de {}'.format(co,ca))
print('O calculo do comprimento da hipotenusa é {:.2f}'.format(hp))

