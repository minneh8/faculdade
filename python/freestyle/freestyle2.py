#Desenvolver o algoritmo e o diagrama de blocos para implementar o cálculo de média aritmética de 3 notas e informar se o aluno está:
# * Aprovado (média ≥ 7)
# * Recuperação (média ≥ 5 e < 7)
# * Reprovado (média < 5)

n1 = float(input("Coloque a sua nota na Prova 1: "))
n2 = float(input("Coloque a sua nota na Prova 2: "))
n3 = float(input("Coloque a sua nota na Prova 3: "))

# Cálculo
mf = (n1 + n2 + n3) / 3

if mf >= 7:
    print("Aprovado")
if mf >= 5 and mf < 7:
    print("Recuperação")
if mf < 5:
    print("Reprovado")