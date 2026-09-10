sets = {1, 2 ,3 ,4}
print(sets)

sets.add(5)
sets.update([6, 7, 8])   

sets.add(3) #Numero que já existe (repetido), não será adicionado

print(sets)

sets.remove(2)     # remove, se o elemento não existir causa erro
sets.discard(99)   #remove, se o elemento não existir não faz nada, sem erro
pop = sets.pop()        # remove e retorna um elemento

print(pop)
print(sets)