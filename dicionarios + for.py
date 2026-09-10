turma = []

for i in range(5):
    turma.append({"nome": input("digite o nome do aluno: "), "nota": float(input("Digite a nota do aluno: "))})
    if turma[i]["nota"] >= 7:
        turma[i].update({"status": "aprovado"})
    elif turma[i]["nota"] >= 5 and turma[0]["nota"] < 7:
        turma[i].update({"status": "recuperação"})
    else:
        turma[i].update({"status": "reprovado"})

#print(turma)

for i in range(5):
    print("nome do aluno: ", turma[i]["nome"])
    print("Nota do aluno: ", turma[i]["nota"])
    print("Status do aluno: ", turma[i]["status"])


