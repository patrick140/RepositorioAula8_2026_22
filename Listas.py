lista = [10, 20, 30, 40]
print(max(lista)) #retorna o maior valor da lista
print(min(lista)) #retorna o menor valor da lista
print(sum(lista)) #retorna a soma de todos os valores da lista

valor = lista.pop(0) #remove na posição retornando o valor
#lista.remove(10) # remove a primeira ocorencia do valor
#del lista[0] # remove o item na posição 0 sem retornar o valor
print(valor)   
print(lista)   

lista.append(50) #insere depois da ultima posição         
lista.insert(0, 10) #insere na posição 0
print(lista)

ultimo = lista.pop() # Sem argumento, remove o último
print(ultimo)  # 40

