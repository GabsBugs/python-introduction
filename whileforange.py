#while
i = 0

while(i<=3):
    print(i)
    print("Gatinhoooooossss")
    i = i+1
    i+=1
#i+=1 é a mesma coisa que i = i+1

for i in "gatinho":
    print(i)

num = [2,5,9,1]

for j in num:
  print(j)

for i in range(20):
  print(i+2)

for j in range(-10,0,2):
  print(j)

'''
range 
primeiro numero = numero de partida
segundo numero = numero de chegada
terceiro numero = em quantos em quantos n vai saltar
'''

#for k in range(0,18,3):
# print(k)

#for t in range(10):
#print(t)
# if (t == 5):
# break 

p = 0
while (p<10):
  p+=1
  if (p%2==0): #número par é ignorado
    continue 
  print(p)