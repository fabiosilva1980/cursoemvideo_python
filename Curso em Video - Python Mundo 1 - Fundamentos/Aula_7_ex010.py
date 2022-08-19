# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# contação do dia do video: R$ 3.27

dinheiro = float(input('Digite o valor em dinheiro R$ : '))
dolar = dinheiro / 3.27
print('Com o valor R$ {:.2f} você pode comprar US$ {:.2f}'.format(dinheiro, dolar))
