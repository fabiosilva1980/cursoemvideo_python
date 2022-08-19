# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario = float(input('Digite o salario: R$ '))
novosalario = salario * 1.15
print('Seu salário era de R$ {:.2f} e com aumento de 15% passará a ser R$ {:.2f}'.format(salario, novosalario))
