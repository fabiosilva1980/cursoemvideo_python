# escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
# Para salários superiores à R$ 1.250,00, calcule 10%.
# Para salários inferiores ou iguais, o aumento é de 15%

sal = float(input('Digite o valor do salario: '))
if sal > 1250:
    aum_sal = sal + (sal * 10 / 100)
else:
    aum_sal = sal + (sal * 15 / 100)
print('Quem ganhava R$ {:.2f} passa a ganhar R${:.2f}'.format(sal, aum_sal))

# Condição Simplificado
sal_aum = sal * 1.10 if sal > 1250 else sal * 1.15
print('Salário atualizado R${:.2f}.'.format(sal_aum))