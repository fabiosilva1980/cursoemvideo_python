# Faça um programa que leia um número de 0 á 9999 e mostre na tela um por um dos digitos separados
# Ex.: Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

numero = int(input('Digite um numero de 0 à 9999: '))
print('Analisando o número {}'.format(numero))
print('Unidade: {}'.format(numero // 1 % 10))
print('Dezena: {}'.format(numero // 10 % 10))
print('Centena: {}'.format(numero // 100 % 10))
print('Milhar: {}'.format(numero // 1000 % 10))

