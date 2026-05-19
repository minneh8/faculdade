arq = open("carros.txt" , "r")
aux = " "
dados = []
somaano = 0
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

tam = len(dados)
for i in range(tam):
    ano = int(dados[i][2])
    somaano = somaano + ano

media = somaano / tam
print(f"A media de Ano dos carros é igual a: {media:.2f}")