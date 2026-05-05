dados = [
    ["ADAMASTHOR", 47, "19 991007899", "M"],
    ["BYTHORYAZ", 18, "19 992139503", "F"],
    ["18000GAMES", 19, "19 923465123", "M"],
    ["ONLAYNY", 20, "19 9093489239", "F"],
    ["OFFLAYNNY", 21, "19 87234672", "F"],
]
homens = []
mulheres = []
for pos,aux in enumerate(dados):
    aux = dados[pos]
    nome = aux[0]
    idade = aux[1]
    celular = aux[2]
    sexo = aux[3]
    if sexo == "M":
        hms = (nome, idade, celular, sexo)
        homens.append(hms)
    elif sexo == "F":
        fmn = (nome, idade, celular, sexo)
        mulheres.append(fmn)
print("\n----------Homens----------")        
for pos,aux in enumerate(homens):
    aux = homens[pos]
    print(f"\nNome: {aux[0]}\nIdade: {aux[1]}\nCelular: {aux[2]}\nSexo: {aux[3]}")

print("\n----------Mulheres----------")
for pos, aux in enumerate(mulheres):
    aux = mulheres[pos]
    print(f"\nNome: {aux[0]}\nIdade: {aux[1]}\nCelular: {aux[2]}\nSexo: {aux[3]}")