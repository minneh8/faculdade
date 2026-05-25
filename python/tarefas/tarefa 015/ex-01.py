
    # Criar arquivo de exemplo para tester o programa:             
with open("NOMEPESO.TXT", "w") as f:
    f.write("Ana Silva\n60.5\nCarlos Souza\n85.0\nMaria Oliveira\n72.3\nJoao Santos\n55.0\nLucia Ferreira\n90.0\n")

    valor = float(input("Digite o peso mínimo para contagem: "))
    contador = 0

    with open("NOMEPESO.TXT", "r") as arquivo:
        linhas = arquivo.readlines()

    i = 0
while i < len(linhas):
    nome = linhas[i].strip()
    peso = float(linhas[i + 1].strip())
    if peso >= valor:
        contador += 1
    i += 2

print(f"\nNúmero de pessoas com peso >= {valor} kg: {contador}")