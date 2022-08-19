n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, m, d))
print('A divisão inteira é {}, a exponenciação é {}'.format(di, e))

print('{:=^30}'.format('Unificar prints'))

# para unificar prints
print('A soma é {}, a multiplicação é {}, a divisão é {:.3f}'.format(s, m, d), end=' ')
print('A divisão inteira é {}, a exponenciação é {}'.format(di, e))

print('{:=^30}'.format('Quebra em linhas'))

# para quebrar em linhas - \n
print('A soma é {}, \n a multiplicação é {}, \n a divisão é {:.3f}'.format(s, m, d))