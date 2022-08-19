# Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada

num = int(input('Digite um número inteiro: '))

for i in {1,2,3,4,5,6,7,8,9,10}:
    tabuada = num * i
    print('{} x {} = {}'.format(num,i, tabuada))
    i =+ 1
