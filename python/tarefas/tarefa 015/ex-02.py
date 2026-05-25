
    # Criar arquivo de exemplo para teste
with open("NOMEPESO.TXT", "w") as f:
    f.write("Ana Silva\n60.5\nCarlos Souza\n85.0\nMaria Oliveira\n72.3\nJoao Santos\n55.0\nLucia Ferreira\n90.0\n")

    valor = float(input("Digite o peso mínimo para seleção: "))

with open("NOMEPESO.TXT", "r") as arquivo:
        linhas = arquivo.readlines()

selecionados = open("SELECIONADOS.TXT", "w")
nao_selecionados = open("NAOSELECIONADOS.TXT", "w")

i = 0
while i < len(linhas):
        nome = linhas[i].strip()
        peso = float(linhas[i + 1].strip())
        if peso >= valor:
            selecionados.write(f"{nome}\n{peso}\n")
        else:
            nao_selecionados.write(f"{nome}\n{peso}\n")
        i += 2

selecionados.close()
nao_selecionados.close()

print(f"\nArquivos gerados com sucesso!")
print("- SELECIONADOS.TXT")
print("- NAOSELECIONADOS.TXT")
