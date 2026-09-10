dicionario = {"primeiro": 1, "segundo": 2, "terceiro": 3}

print(dicionario.values())

del dicionario["terceiro"]              # remove a chave (KeyError se não existir)
valor = dicionario.pop("segundo")       # remove e retorna o valor (25)
dicionario.pop("primeiro", None)        # remove com padrão (não dá erro)
#item = dicionario.popitem()           # remove e retorna o último par (LIFO)
#dicionario.clear()

dicionario.update({"quarto": 4})

print(dicionario.values())