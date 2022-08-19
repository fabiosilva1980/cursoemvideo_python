# Condição

# Estrutura condicional simples - IF
# Estrutura condicional composta - IF ELSE

# Exemplo 1:
tempo = int(input('Quantos anos tem o seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

# Exemplo 2 - Condição Simplificada
tempo = int(input('Quantos anos tem o seu carro? '))
print('Carro Novo'if tempo <=3 else 'Carro Velho')
print('--FIM--')

# Prática 1 - Condição Simples
nome = str(input('Qual o seu nome? '))
if nome == 'Fabio':
    print('Que lindo nome!')
print('Bom dia, {}.'.format(nome))

#Prática 2 - Condição Composta
sobrenome = str(input('QUal o seu sobrenome? '))
if sobrenome == 'Silva':
    print('Seu sobrenome é comum')
else:
    print('Seu sobrenome é diferente!')
print('Tudo bem {} {}.'.format(nome, sobrenome))

#Pratica 3 - Condiçãp Somplificada
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('Sua média foi {:.1f}.'.format(m))
#if m >= 6.0:
#    print('Sua foi média foi boa, PARABÉNS!')
#else:
#    print('Sua média foi ruim, ESTUDE MAIS!')
print('PARABÉNS!' if m >= 6.0 else 'ESTUDE MAIS!')