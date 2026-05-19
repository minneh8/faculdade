arq = open("carros.txt" , "r")
aux = " "
dados = []

while aux != "":
    aux = arq.readline()
    if aux != "":
        aux = aux.strip("\n")
        reg = aux.split(",")
        marca = reg[0]
        modelo = reg[1]
        ano = int(reg[2])
        cor = reg[3]
        placa = reg[4]
        print(f"Marca: {marca}\nModelo: {modelo}\nAno: {ano}\nCor:{cor}\nPlaca: {placa}\n")
        dadosaux = [marca, modelo, ano, cor, placa]
        dados.append(dadosaux)