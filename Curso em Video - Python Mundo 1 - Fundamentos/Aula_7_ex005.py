# Escreva um programa que leia um número inteiro e demostre em tela seu sucessor e seu antecessor
num = int(input('Digite um numero inteiro: '))
antec = num -1
suces = num +1

print('O numero digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(num, antec,suces))
print('O numero digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(num, (num - 1),(num + 1)))

