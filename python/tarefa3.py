#Desenvolver o algoritmo e o diagrama de blocos para implementar o cálculo do salario bruto, imposto de renda (percentual único e fixo) e o salario fixo

sh = float(input("Qual o seu salario por hora ?"))
ht = int(input("Quantas horas trabalhadas ?"))
ir = 15

#Cálculo
sb = sh * ht
irp = sb * ir / 100
sl = sb - irp

print("o salario bruto é", sb, "e o salario liquido, com o imposto de renda aplicado é", sl)