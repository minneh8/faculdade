import pandas as pd
df = pd.read_csv("carros.csv", delimiter = ",")
for reg in df:
    print(reg)

colunas = df.columns
print(f"Colunas: {colunas}")

tam = len(df)
for pos in range(0, tam):
     print("MARCA:    ", df["MARCA"][pos])
     print("MODELO:   ", df["MODELO"][pos])
     print("ANO:      ", df["ANO"][pos])
     print("COR:      ", df["COR"][pos])
     print("PLACA:    ", df["PLACA"][pos])
