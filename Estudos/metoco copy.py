lista = [40, 30, 20] #.retonar uma lista igual mas não é a mesma lista, 
#exemplo usando ID você consegue ver numeros diferentes

print(lista)

l2 = lista.copy()

print(id(l2), id(lista))