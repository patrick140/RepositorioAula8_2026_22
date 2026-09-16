dicionario = {"primeiro": 1, "segundo": 2, "terceiro": 3}

print(dicionario.values())
print(dicionario.keys())
print(dicionario.items())

del dicionario["terceiro"]              # remove a chave (KeyError se não existir)
valor = dicionario.pop("segundo")       # remove e retorna o valor (25)
valor = dicionario.pop("kkk", "essa chave não existe") # remove com padrão (não dá erro)
#item = dicionario.popitem()           # remove e retorna o último par 
#dicionario.clear()

dicionario.update({"quarto": 4})




