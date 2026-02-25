# Desenvolver um software para o calculo do cambio de moedas
vd = float(input("quantos rapid voce quer transformar em dolar ?"))
print("O valor do dolar nessa cotação esta em 3,00 rapid")
dl = 3.0

#Cálculo
cv = (vd + 10) / dl
txa = cv - ((2 * cv )/ 100)
imr = txa - ((0.6 * txa) / 100)

print("O valor em dolar para a quantia que vocé deseja converter é:", txa)
print("O valor em dolar para a quantia que vocé deseja converter com 0.6 de imposto de renda é:", imr)