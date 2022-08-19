# Crie um programa que leia um número e mostre se ele é PAR ou ÍMPAR.
num = int(input('Digite um numero: '))
resto = num % 2

if resto == 0:
    print('Este numero é par!')
else:
    print('Este numero é impar')
