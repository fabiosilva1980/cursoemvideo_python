# Escreva um programa que leia a velocidade de um carro.
# Se a velocidade ultrapassar 80 km/h. mostre uma mensaggem dizendo que ele foi multado.
# A multa vai custar R$ 7.00 por cada km acima do limite.

vel = float(input("Digite a velocidade do carro: "))

if vel > 80:
    multa = (vel - 80) * 7
    print('MULTADO!!! Você ultrapassou o limite de velocidade da via')
    print('Sua multa é de R${:.2f}.'.format(multa))
print('Lembre-se - Dirija com segurança! \nTenha uma boa viagem')
