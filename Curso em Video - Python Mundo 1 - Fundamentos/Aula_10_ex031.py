# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$ 0.50 por Km para viagens de até 200 Km e
# R$ 0.45 para viagens mais longas.

distancia = float(input('Qual a distancia da viagem em km. ? '))

if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('O valor da passagem para esta viagem de {:.0f}km é de R${:.2f} .'.format(distancia, passagem))

# condição simplificada
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('O valor da passagem para esta viagem de {:.0f}km é de R${:.2f} .'.format(distancia, preco))
