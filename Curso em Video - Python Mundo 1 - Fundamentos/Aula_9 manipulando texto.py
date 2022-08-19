frase = "Curso em video Python"
# Curso em Video Python - possui 21 caracteres e sua contagem começa em 0
# 01234567891011121314151617181920
print(frase)

# Fatiamento de string
print(frase[3])         # irá printar apenas o caracter 6 da frase
print(frase[9:13])      # irá printar a range de caracteres de 9 a 12
print(frase[9:21])      # irá printar o range de 9 a 20 mesmo que o 21º caracter não exista
print(frase[9:21:2])    # irá printar o range de caracteres de 9 a 20 pulando de 2 em 2 caracteres
print(frase[15:])       # irá fatiar a frase apartir do 15 até o final
print(frase[9::3])      # irá começar no caracter 9 e vai até o final pulando de 3 em 3 caracteres

# Analise de string
print(len(frase)) # irá printar analisar a quantidade de caracteres
print(frase.count('o')) # irá printar contar a quantidade de vezes que o caracter "o" aparece (case sensitive)
print(frase.find('deo')) # irá printar encontrar/mostrar em que casa começa a string "deo" na frase.
print(frase.find('Android')) # não será encontrada na frase e retorna (print) o valor "-1"
print('Curso' in frase) # irá printar utilizando o operador IN para validar se a string "Curso" existe na variável frase

# Transformação
print(frase.replace('Python','Android')) # irá printar efetuando a troca de forma secundaria a string "Python" por "Android"
print(frase.upper()) # irá printar trocando todos os caracteres para maiúsculo
print(frase.lower()) # irá printar trocando todos os caracteres para minúsculo
print(frase.capitalize()) # irá printar colocando todos os caracteres em minúsculo e somente o primeiro caracter será maiúsculo
print(frase.title()) # irá printar colocando toda a string em minúsculo e somente o primeiro caracter em cada
# elemento (separado por espaços) será maiúsculo
frase2 = '   Aprenda Python  '
print(len(frase2))
print(frase2.strip()) # remove todos os espaços excedentes na string
print(len(frase2.strip())) # contagem com os espaços removidos
print(frase2.rstrip()) # remove os espaços excedentes na direta da string
print(frase2.lstrip()) # remove os espaços excedentes na esquerda da string
# A mudança na string só pode ser feita após salvar o resultado da transformação
# frase = frase.replace("Python", "Android")

# Divisão na string
dividido = frase.split() # divide a string utilizando o espaço com delimitador e coloca cada elemento dentro de uma lista
print(dividido)
# ler sobre a função split()
print(dividido[0]) # irá printar o elemento 0 na lista "dividido"
print(dividido[2][3]) # irá printar o caracter 3 no elemento 2 na lista "dividido"

# Junção
print('-'.join(dividido)) # faz a junção dos elementos com adicionando o delimitar "-" a string


