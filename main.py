lista = [1,2,3,4,4,5,5,7,13,23,1]

newList = []

for x in lista:
    if x not in newList:
        newList.append(x)
print(newList)

novalista = []
novalista = set(lista)
print(novalista)

