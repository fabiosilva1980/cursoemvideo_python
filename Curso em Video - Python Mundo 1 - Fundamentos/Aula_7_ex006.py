# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e sua raiz quadrada

num = int(input('Digite um valor inteiro: '))
dobro = num * 2
triplo = num * 3
quadrada = num ** 0.5 # ou (1/2) ou Power - pow(num, (1/2))

print('O número digitado foi {}, o dobro do é {}.'.format(num,dobro))
print('O triplo é {} e \na raiz quadrada é {:.2f}.'.format(triplo,quadrada))

# outra forma
print('O número digitado foi {}, o dobro do é {}.'.format(num,(num*2)))
print('O triplo é {} e \na raiz quadrada é {:.2f}.'.format((num*3),(num**(1/2))))
