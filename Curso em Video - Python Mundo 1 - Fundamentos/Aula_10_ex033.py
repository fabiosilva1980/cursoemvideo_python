# Faça um programa que leia três numeros e mostre qual é o MAIOR e qual é o MENOR.
n1 = int(input('Primeiro número:'))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

# Verificando o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O valor maior é {} e o menor valor é {}.'.format(maior,menor))

