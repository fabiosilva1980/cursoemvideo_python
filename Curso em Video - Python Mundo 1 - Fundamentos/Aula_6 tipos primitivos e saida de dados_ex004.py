# Faça um programa que leia algo pelo teclado e mostre na tela o seu estado primitivo
# e todas as informações possíveis sobre ela.

n = input('Digite algo: ')
print('o tipo primitivo desse valor é',type(n))
print('Só tem espaços? ',n.isspace())
print('É um número? ',n.isnumeric())
print('É alfabético? ',n.isalpha())
print('É alfanumérico? ',n.isalnum())
print('Está em maiúsculo? ',n.isupper())
print('Está em minúsculo? ',n.islower())
print('Está capitalizado? ',n.istitle())

# parte extra
print('O tipo primitido deste valor é {}, ele tem espaços {}, é um numero {}, é alfabético {}, é alfanumerico {}, está em maiúsculo {}, está em minusculo {}, esta capitalizado {}'.format(type(n),n.isspace(), n.isnumeric(), n.isalpha(), n.isalnum(), n.isupper(), n.islower(), n.istitle()))

