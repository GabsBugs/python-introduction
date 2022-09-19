l = 'lista de letras'
data = '17/09/2022'

#tamanho(len)
tamanho = len(l)
print(tamanho)
#lista de letras = l = possui 15 letras (len)

#split, pedaços da string
lista = l.split (" ")
lista2 = data.split ("/")
print(lista)
print(lista2)

#substituição(replace)
print(l.replace(' de ','')) #substituiu o 'de' por nada

#      -5-4-3-2-1
#       012345
nome = 'python'

nova_string = nome[1:4]
print(nova_string)

print("a" == "b")
print("a" > "X")

#tabela ASCII

for m in range(122):
    print(str(m) + ' - ' + chr(m))

#percorrer com for
for f in nome:
    print(f)

#percorrer com while
s = 0
while s < len(nome):
    print(nome[s])
    s+=1

#percorrer com for / enumerate
for k,v in enumerate(nome):
    print(k,v)

alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'

for n,m in enumerate(alphabet):
    print(n,m)
print(alphabet.replace(' ', '-'))