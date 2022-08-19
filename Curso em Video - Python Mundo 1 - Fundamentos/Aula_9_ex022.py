# Crie um programa que leia o nome completo de uma pessoa e mostre:
# * O nome com todas as letras maiúsculas
# * O nome com todas as letras minúsculas
# * Quantas letras tem ao nome (sem contar os espaços)
# * Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: '))
print('Analisando o nome...')
print('Seu nome em letras maísculas fica {}'.format(nome.upper()))
print('Seu nome em letras minusculas fica {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome.replace(' ',''))))
dividido = nome.split()
print('Seu primeiro nome é {} e possui {} letras'.format(dividido[0], len(dividido[0])))
