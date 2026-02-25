#Desenvolver um Software para o calculo de cada refeição em relação do numero de porcoes degustadas
print("O preço da porção em RP$ (Rapydyz) é 50,00")

pc = int(input("Quantas porcoes vocé degustou ? "))
pp = 50.00

#Cálculo
sbt = pp * pc
ds = pp * 2 / 100
slt = sbt - ds
tx = slt - (slt * 10 / 100)
sl = tx

print("O valor da refeição em RP$ (Rapydyz) é:", sl)

