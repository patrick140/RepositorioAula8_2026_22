dicionario = {}

dicionario.update({"nome": input("Digite o nome do aluno: ")})

dicionario.update({"nota": float(input("Digite a nota do aluno: "))})

if dicionario["nota"] >= 7:
    dicionario.update({"status": "aprovado"})
elif dicionario["nota"] >= 5 and dicionario["nota"] < 7:
    dicionario.update({"status": "recuperação"})
else:
    dicionario.update({"status": "reprovado"})

print(dicionario)