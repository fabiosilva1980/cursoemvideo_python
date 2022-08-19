# Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto

produto = float(input('Digite o preço do produto: R$ '))
novopreco = produto - (produto * 0.05)
print('O valor do produto é R$ {:.2f}, com o desconto de 5% ficaria R$ {:.2f}'.format(produto,novopreco))
