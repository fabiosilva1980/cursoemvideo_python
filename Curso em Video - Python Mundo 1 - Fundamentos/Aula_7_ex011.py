# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro pinta uma área de 2m²

altura = float(input('Digite a altura em metros: '))
largura = float(input('Digite a largura em metros: '))

area = altura * largura
tinta = area / 2

print('Para pintar uma parede de {}m², você precisará de {}lts de tinta para pintá-la'.format(area, tinta))
