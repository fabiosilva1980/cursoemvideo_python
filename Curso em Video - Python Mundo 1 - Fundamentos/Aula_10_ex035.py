# Desenvolva um programa que leia um comprimento de três retas e
# diga ao usuário se elas podem ou não formar um triângulo
print('=+=' * 20)
print('Analizador de triângulos')
print('=+=' * 20 )
r1 = float(input('Digite o comprimento da primeiro segmento: '))
r2 = float(input('Digite o comprimento do segundo segmento: '))
r3 = float(input('Digite o comprimento do terceiro segmento: '))

# soma dos 2 segmentos deve ser menor que o terceiro

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triângulo!')
else:
    print('Os segmentos não podem formar um triângulo.')
