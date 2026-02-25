#Desenvolver um Software para o calculo do salario liquido
sh = float(input("DIgite seu Salario hora: "))
ht = float(input("Digite o numero de horas trabalhadas: "))

#Cálculo
sb = sh * ht
da = sb * 10 / 100
ir = sb * 5 / 100
sl = sb - da - ir

print("O salario liquido é:", sl)