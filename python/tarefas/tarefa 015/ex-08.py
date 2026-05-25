# Criar arquivo de exemplo para teste
with open("NEYRIOMECYCARDIO.TXT", "w") as f:
        for valor in [72, 85, 91, 68, 77, 95, 60, 88, 73, 82]:
            f.write(f"{valor}\n")
 
batimentos = []
 
with open("NEYRIOMECYCARDIO.TXT", "r") as arquivo:
        for linha in arquivo:
            valor = linha.strip()
            if valor:
                batimentos.append(int(valor))
 
if not batimentos:
        print("Arquivo vazio ou sem dados válidos.")
 
media = sum(batimentos) / len(batimentos)
minimo = min(batimentos)
maximo = max(batimentos)
 
print("=== Análise de Batimentos Cardíacos - Neyrio Meçy ===\n")
print(f"Total de leituras : {len(batimentos)}")
print(f"Média             : {media:.2f} bpm")
print(f"Mínimo            : {minimo} bpm")
print(f"Máximo            : {maximo} bpm")