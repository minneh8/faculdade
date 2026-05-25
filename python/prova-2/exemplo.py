

arq = open("exemplo.txt", "r")
vacina = open("vacinados.txt", "w")
Nvacinados = open("Nvacinados.txt", "w")
homem = 0
mulher = 0
vacinadosM = 0
nao_vac_homem = 0
nao_vac_mulher = 0
vacinadosF = 0
covidM = 0
covidF = 0
total = 0

for linha in arq:
    dados = linha.split("|")
    sexo = dados[1]
    vacinados = dados[4]
    covid = dados[3]
    if sexo == "M" or sexo == "m":
        if vacinados == "S" or vacinados == "s":
            vacinadosM += 1
            vacina.write(f"{linha}\n")
        else:
            nao_vac_homem += 1
            Nvacinados.write(f"{linha}\n")
        if covid == "S" or covid == "s":
            covidM += 1
    if sexo == "F" or sexo == "F":
        if vacinados == "S" or vacinados == "s":
            vacinadosF += 1
            vacina.write(f"{linha}\n")
        else:
            nao_vac_mulher += 1
            Nvacinados.write(f"{linha}\n")
        if covid == "S" or covid == "s":
            covidF += 1
    total += 1
    arq.close()
    vacina.close()
    Nvacinados.close()
media = vacinadosF + vacinadosM / total

print(f"Total de pessoas: {total}")
print(f"Total de vacinados masculino: {vacinadosM}")
print(f"Total de pessoas sem vacina masculino: {nao_vac_homem}")
print(f"Total de vacinados feminino: {vacinadosF}")
print(f"Total de pessoas com Covid masculino: {covidM}")
print(f"Total de pessoas com Covid feminino: {covidF}")
print(f"Media de vacinados: {media}")