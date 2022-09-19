#dictionary = {'a' : 'amor', 'b' : 'baixinho'}
#dictionary2 = {(10,20):['luna','gatinho',30]}

#print(dictionary['a'])
#print(type(dictionary))
#print(dictionary.get('d', 'valor não encontrado.'))

#del é para remover
#del(dictionary['a'])
#print(dictionary)

#print(dictionary.keys())
#print(dictionary.values())
#print(len(dictionary))

#popitem remove o último item
#print(dictionary.popitem())
#print(dictionary.popitem())
#print(dictionary)

semana = {'dia1':'domingo','dia2':'segunda','dia3':'terça','dia4':'quarta','dia5':'quinta','dia6':'sexta','dia7':'sabádo'}
print(semana.popitem())
print(semana.popitem())
del(semana['dia2'])

print(semana.keys())
print(semana.values())

print(semana)
