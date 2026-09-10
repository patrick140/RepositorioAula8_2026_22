lista = []

for i in range(5):
    valor = float(input("Digite um numero: "))
    lista.append(valor)

print("O maior valor da lista é: ", max(lista))
#print(f"{max(lista)} é o maior valor da lista" )

print("O menor valor da lista é: ", min(lista))
#print(f"{min(lista)} é o menor valor da lista")

print("A soma dos valores da lista é: ", sum(lista))
#print(f"{sum(lista)} é a soma dos valores da lista")

lista_tupla_protegida = tuple(lista) # cria uma tupla cujo valor é os valores na lista