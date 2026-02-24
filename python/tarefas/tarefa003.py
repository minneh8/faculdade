#Desenvolver um Software para o calculo de venda com ou sem desconto


qv = int(input("Digite o valor da quantidade de vendas: "))
pu = float(input("Digite o valor do preco unitario: "))

#Cálculo
vb = qv * pu

if vb > 1000:
    pv = vb - (vb * 0.1)
    print("O valor da venda com 10 porcento de desconto é:", pv)
else:
    print("O valor da venda sem desconto é:", vb)