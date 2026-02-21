#Desenvolver um Software para o calculo de cada refeição em relação do numero de porcoes degustadas
print("O preço da porção em RP$ - Rapydyz é 50,00")

pc = int(input("Quantas porcoes vocé degustou ? "))
pp = 50.00

#Cálculo
sbt = pp * pc
if pc == 1:
    dsc = sbt - (sbt * 2 / 100)
    cca = dsc + 20.00
    tt = cca + (cca * 10 / 100)
    print ("O valor total da refeição com o desconto de dois porcento a cada porção e a taxa de serviço de 10% é:", tt)
if pc == 2:
    dsc = sbt - (sbt * 4 / 100)
    cca = dsc + 20.00
    tt = cca + (cca * 10 / 100)
    print ("O valor total da refeição com o desconto de dois porcento a cada porção e a taxa de serviço de 10% é:", tt)
if pc == 3:
    dsc = sbt - (sbt * 6/ 100)
    cca = dsc + 20.00
    tt = cca + (cca * 10 / 100)
    print ("O valor total da refeição com o desconto de dois porcento a cada porção e a taxa de serviço de 10% é:", tt)
if pc == 4:
    dsc = sbt - (sbt * 8 / 100)
    cca = dsc + 20.00
    tt = cca + (cca * 10 / 100)
    print ("O valor total da refeição com o desconto de dois porcento a cada porção e a taxa de serviço de 10% é:", tt)

