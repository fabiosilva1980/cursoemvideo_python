# Crie um programa que leia o nome dela e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: ')).strip()
print('É','SILVA' in nome.upper(), 'que seu nome contem "Silva"')