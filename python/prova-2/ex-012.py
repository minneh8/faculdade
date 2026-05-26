dados = []
arq = open("cadastro.txt", "r")
arq2 =  open("selecionados.txt", "w")
for linha in arq:
    linha = linha.split(",")
    id = int(linha[0])
    nome = linha[1]
    idade = int(linha[2])
    altura = float(linha[3])
    peso = float(linha[4])
    sexo = linha[5]
    estadocivil = linha[6]
    numerofilhos = int(linha[7])
    escolaridade = linha[8]
    if idade >= 20 and idade <= 30:
        if altura >= 1.60 and altura <= 1.80:
            if peso >= 60 and peso <= 80:
                if escolaridade == "SP":   
                    dados.append([id, nome, idade, altura, peso, sexo, estadocivil, numerofilhos, escolaridade])
                    arq2.write(str(dados))

arq.close()
arq2.close()