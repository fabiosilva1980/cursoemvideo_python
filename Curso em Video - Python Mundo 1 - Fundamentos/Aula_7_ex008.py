# Escreva um programa que leia um valor em metros e o exiba convertido em centrimetros e milimetros

metros = int(input('Digite o valor em metros: '))
centimetros = metros * 100
milimetros = metros * 1000

print('O valor em metros é {}, convertido em centrimetros é {}cm e convertido em milimetros é {}mm'.format(metros, centimetros, milimetros))