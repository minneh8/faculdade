dados = [
    ["8000games", 1.71, 105],
    ["Joao", 1.30, 94],
    ["Adamastor", 1.50, 99],
    ["Zago", 1.66, 35]
]

pos = 0
tam = len(dados)
while pos < tam:
    imc = dados[pos][2] / (dados[pos][1] ** 2)
    print(f"Nome: {dados[pos][0]} /  Altura: {dados[pos][1]} / Peso: {dados[pos][2]} / IMC: {imc}")
    pos = pos + 1