def main():
    # Criar arquivo de exemplo para teste
    # Estrutura: batimento, pressao, temperatura, sudorese (repetindo por leitura)
    dados_exemplo = [
        (72, 120, 36.5, 2),
        (85, 130, 37.1, 4),
        (91, 140, 37.8, 6),
        (68, 115, 36.2, 1),
        (77, 125, 36.9, 3),
        (95, 145, 38.0, 7),
    ]
    with open("NEYRIOMECYGERAL.TXT", "w") as f:
        for d in dados_exemplo:
            f.write(f"{d[0]}\n{d[1]}\n{d[2]}\n{d[3]}\n")
 
    batimentos = []
    pressoes = []
    temperaturas = []
    sudoreses = []
 
    with open("NEYRIOMECYGERAL.TXT", "r") as arquivo:
        linhas = arquivo.readlines()
 
    i = 0
    while i + 3 < len(linhas):
        batimentos.append(float(linhas[i].strip()))
        pressoes.append(float(linhas[i + 1].strip()))
        temperaturas.append(float(linhas[i + 2].strip()))
        sudoreses.append(float(linhas[i + 3].strip()))
        i += 4
 
    def estatisticas(lista, nome, unidade=""):
        media = sum(lista) / len(lista)
        print(f"\n{nome}:")
        print(f"  Média  : {media:.2f}{unidade}")
        print(f"  Mínimo : {min(lista):.2f}{unidade}")
        print(f"  Máximo : {max(lista):.2f}{unidade}")
 
    print("=== Análise Biométrica - Neyrio Meçy (TECA) ===")
    estatisticas(batimentos, "Batimento Cardíaco", " bpm")
    estatisticas(pressoes, "Pressão Arterial", " mmHg")
    estatisticas(temperaturas, "Temperatura", " °C")
    estatisticas(sudoreses, "Nível de Sudorese")
 
main()
 