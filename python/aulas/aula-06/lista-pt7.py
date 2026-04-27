dados = [
    ["Antenor", 3000, 9, 9],
    ["Zago", 4000, 7, 6],
    ["Eduardo", 3500, 2, 4],
    ["Matheus",4500, 6, 5],
    ["Joao", 300, 7, 4]
]

pos = 0 
tam = len(dados)
while pos < tam:
    media = (dados[pos][2] + dados[pos][3]) / 2
    if media < 5:
        print(f"Nome: {dados[pos][0]} / Mensalidade: {dados[pos][1]} / Nota 1: {dados[pos][2]} / Nota 2: {dados[pos][3]} / Media: {media} / Desconto: 0% \n Mensalidade com o Desconto: {dados[pos][1]}\n")
    elif media >= 5 and media < 7:
        desconto = dados[pos][1] - (dados[pos][1] * 5) / 100
        print(f"Nome: {dados[pos][0]} / Mensalidade: {dados[pos][1]} / Nota 1: {dados[pos][2]} / Nota 2: {dados[pos][3]} / Media: {media} / Desconto: 5% \n Mensalidade com o Desconto: {desconto}\n")
    elif media >= 7 and media < 9:
        desconto = dados[pos][1] - (dados[pos][1] * 10) / 100
        print(f"Nome: {dados[pos][0]} / Mensalidade: {dados[pos][1]} / Nota 1: {dados[pos][2]} / Nota 2: {dados[pos][3]} / Media: {media} / Desconto: 10% \n Mensalidade com o Desconto: {desconto}\n")
    elif media >= 9 and media <= 10:
        desconto = dados[pos][1] - (dados[pos][1] * 25) / 100
        print(f"Nome: {dados[pos][0]} / Mensalidade: {dados[pos][1]} / Nota 1: {dados[pos][2]} / Nota 2: {dados[pos][3]} / Media: {media} / Desconto: 25% \n Mensalidade com o Desconto: {desconto}" )
    pos = pos + 1