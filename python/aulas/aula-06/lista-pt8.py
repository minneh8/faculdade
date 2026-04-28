dados = [
    ["Antenor", 23, 1.80, 77],
    ["Zago", 56, 1.75, 89],
    ["Eduardo", 12, 1.60, 56],
    ["Matheus",55, 1.70, 76],
    ["Joao", 89, 1.85, 99]
]
pos = 0
tam = len(dados)
while pos < tam:
    imc = dados[pos][3] / (dados[pos][2] * dados[pos][2])
    
    print(f"Nome: {dados[pos][0]} / Idade: {dados[pos][1]} / Altura: {dados[pos][2]} / Peso: {dados[pos][3]} / IMC: {imc:.2f} \n")
    pos += 1