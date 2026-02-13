# Desenvolver um software para calcular o valor das parcelas de uma seguradora de veiculos 

vva = float(input("digite o valor do veiculo : "))
nu = float(input ("digite o numero de usuarios do carro :"))
ts = 15
td = 5
np = int(input ("digite o numero de parcelas desejadas :"))

#Calculo
vst = vva * (ts / 100)
vaps = vst * (nu / 100)
sd = (vst + vaps) * (td / 100)
vrs = vst + vaps - sd
vp = vrs / np

print("O valor da parcela é", vp)