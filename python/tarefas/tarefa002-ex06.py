cmp = float(input("Digite o custo da materia prima: "))
cmo = float(input("Digite o custo da mao de obra: "))
ce = float(input("Digite o custo da energia: "))
cf = float(input("Digite o custos fixos: "))

#Cálculo
ct = cmp + cmo + ce + cf

#Impostos
ir = ct * 27.5 / 100
iof = ct * 3.5 / 100
pv = ct + ir + iof

print("O custo total do projeto é:", ct)
print("O imposto de renda aplicado ao custo total do projeto é:", ir)
print("O imposto da operação financeira aplicado ao custo total do projeto é:", iof)
print("O custo total do projeto com os impostos aplicados é:", pv)
