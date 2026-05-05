dados = [
    ["ADAMASTHOR", 47, "19 991007899", "M"],
    ["BYTHORYAZ", 18, "19 992139503", "F"],
    ["18000GAMES", 19, "19 923465123", "M"],
    ["ONLAYNY", 20, "19 9093489239", "F"],
    ["OFFLAYNNY", 21, "19 87234672", "F"],
]
tam = len(dados)
for pos, aux in enumerate(dados):
    aux = dados[pos]
    nome = aux[0]
    idade = aux[1]
    celular = aux[2]
    sexo = aux[3]
    print(f"\nNOME: {nome}\nIDADE: {idade}\nCELULAR: {celular}\nSEXO: {sexo}")