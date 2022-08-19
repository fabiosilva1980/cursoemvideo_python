# Crie um programa que leia um nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome da cidade: ')).strip() # remove os espaços excedentes digitados

cidade = cidade.upper()
print(cidade.find('SANTO'))
teste = cidade.split()
elemento1 = teste[0]
print(elemento1.find('SANTO'))

print('É','SANTO' in cidade, 'que o nome da cidade começa com "SANTO"')

# correção
print('É {} que o nome da cidade começa com "SANTO".'.format(cidade[:5].upper() == 'SANTO'))
