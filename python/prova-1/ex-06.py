frase = input("Digite uma frase: ")
nchar = len(frase)

total = 0
virgula = 0
ponto = 0
interrogacao = 0
hashtag = 0
pos = 0

while(pos < nchar):
    if frase[pos] == ",":
        virgula = virgula + 1
    elif frase[pos] == ".":
        ponto = ponto + 1
    elif frase[pos] == "?":
        interrogacao = interrogacao + 1
    elif frase[pos] == "#":
        hashtag = hashtag + 1
    pos = pos + 1

total = virgula + ponto + interrogacao + hashtag
porcV = virgula * 100 / total
porcP = ponto * 100 / total
porcI = interrogacao * 100 / total
porcH = hashtag * 100 / total

print("-------------------------------------------")
print(f"Total de caracteres: {total}")
print("-------------------------------------------")
print(f"Porcentagem de virgulas: {porcV :0.2f}%")
print(f"Porcentagem de pontos: {porcP :0.2f}%")
print(f"Prorcentagem de interrogacoes: {porcI :0.2f}%")
print(f"Porcentagem de hashtags: {porcH :0.2f}%")

