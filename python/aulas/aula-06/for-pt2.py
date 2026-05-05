dados = [
    ["ADAMASTHOR", 47, "19 991007899", "M"],
    ["BYTHORYAZ", 18, "19 992139503", "F"],
    ["18000GAMES", 19, "19 923465123", "M"],
    ["ONLAYNY", 20, "19 9093489239", "F"],
    ["OFFLAYNNY", 21, "19 87234672", "F"],
]

#Listar os dados de uma lista de lista
#Contar o numero de M e de F
#Calcular a idade media 
#Indicar o numero de pessoas com a idade maior que 20 anos e menor que 20 anos 
somaidade = 0
sm = 0
sf = 0
mais20 = 0
menos20 = 0
tam = len(dados)
for pos, aux in enumerate(dados):
    aux = dados[pos]
    nome = aux[0]
    idade = aux[1]
    celular = aux[2]
    sexo = aux[3]
    if sexo == "M":
        sm += 1 
    if sexo == "F":
        sf += 1
    if idade >= 20:
        mais20 += 1
    if idade < 20: 
        menos20 += 1
    somaidade += idade
    print(f"\nNOME: {nome}\nIDADE: {idade}\nCELULAR: {celular}\nSEXO: {sexo}")
    

media = somaidade / tam

print(f"\nTem {mais20} pessoas com mais de 20 anos e {menos20} com menos de 20 anos")
print(f"\ntem {sm} Pessoas do Sexo Masculino e {sf} do Sexo Feminino")
print(f"\nA media de idade é igual a: {media}")